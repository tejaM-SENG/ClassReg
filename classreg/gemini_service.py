from pathlib import Path
import re
from difflib import SequenceMatcher

from django.conf import settings
from google import genai

client = genai.Client(api_key=settings.GEMINI_API_KEY)

FAQ_FILE = Path(__file__).resolve().parent / "classhub_faqs.txt"

CONTACT_PHONE = "+91 9876543210"
CONTACT_EMAIL = "support@classhub.com"


def normalize(text):
    """Normalize text for FAQ matching."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return " ".join(text.split())


def load_faqs():
    """Read FAQs formatted as Q: ... and A: ..."""
    if not FAQ_FILE.exists():
        return []

    content = FAQ_FILE.read_text(encoding="utf-8")

    pattern = re.compile(
        r"Q:\s*(.*?)\s*\nA:\s*(.*?)(?=\n\s*Q:|\Z)",
        re.IGNORECASE | re.DOTALL,
    )

    return [
        (match.group(1).strip(), match.group(2).strip())
        for match in pattern.finditer(content)
    ]



def search_documents(question):
    """Return an FAQ answer only when the question is a strong match."""
    faqs = load_faqs()
    question_normalized = normalize(question)

    if not question_normalized:
        return None

    question_words = set(question_normalized.split())
    best_answer = None
    best_score = 0

    for faq_question, faq_answer in faqs:
        faq_normalized = normalize(faq_question)
        faq_words = set(faq_normalized.split())

        # Exact match
        if question_normalized == faq_normalized:
            return faq_answer

        # Require meaningful shared words, not just a loose similarity.
        shared_words = question_words & faq_words

        if not shared_words:
            continue

        # Ignore common words that don't help identify the topic.
        stop_words = {
            "how", "do", "i", "the", "a", "an", "is", "are",
            "can", "to", "my", "for", "what", "and", "on",
            "in", "of", "me", "it", "please"
        }

        meaningful_shared = shared_words - stop_words

        if not meaningful_shared:
            continue

        coverage = len(meaningful_shared) / max(
            1, len(question_words - stop_words)
        )

        similarity = SequenceMatcher(
            None, question_normalized, faq_normalized
        ).ratio()

        score = max(coverage, similarity)

        if score > best_score:
            best_score = score
            best_answer = faq_answer

    # Be conservative to avoid returning unrelated answers.
    if best_score >= 0.65:
        return best_answer

    return None


def is_classhub_question(question):
    """Identify questions about ClassHub services and policies."""
    text = normalize(question)

    keywords = [
        "classhub", "register", "registration", "enroll",
        "enrollment", "fee", "fees", "tuition", "schedule",
        "deadline", "instructor", "course", "class availability",
        "payment", "refund", "class policy", "available classes",
    ]

    return any(keyword in text for keyword in keywords)


def get_classhub_response(question):
    # Step 1: Search the FAQ without using AI.
    faq_answer = search_documents(question)

    if faq_answer:
        return faq_answer

    # Step 2: Do not invent ClassHub-specific information.
    if is_classhub_question(question):
        return (
            "I'm an AI assistant and couldn't verify that information. "
            f"Please contact the ClassHub administrator at "
            f"{CONTACT_PHONE} or {CONTACT_EMAIL}."
        )

    # Step 3: Use Gemini only for general questions.
    prompt = f"""
Answer this general question in 2-3 short sentences.
Use simple, friendly language and complete sentences.

Question: {question}

Return only the answer.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "max_output_tokens": 120,
            "temperature": 0.2,
        },
    )

    answer = (response.text or "").strip()

    if not answer:
        raise ValueError("Gemini returned an empty response.")

    return answer


