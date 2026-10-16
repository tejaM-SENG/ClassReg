from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from classreg.models import Parent, Contact, Student, ClassEnrollment, RegisteredClass
from classreg.forms import ParentForm, ContactForm, StudentForm, ParentProfileForm, RegisteredClassForm, StudentProfileForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login
from django.db import transaction
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.http import require_POST
from django.db.models import Count
from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .gemini_service import get_classhub_response
import logging
from django.db.models.deletion import ProtectedError


User = get_user_model()

# Create your views here.

def home(request):
    return render(request, 'classreg/home.html', {'student_form': StudentForm()})

def about(request):
    return render(request, 'classreg/about.html')

def python(request):
    return render(request, 'classreg/python.html')

def java(request):
    return render(request, 'classreg/java.html')

def django(request):
    return render(request, 'classreg/django.html')

def photos(request):
    return render(request, 'classreg/photos.html')

def videos(request):
    return render(request, 'classreg/videos.html')

def contact(request):
    f=ContactForm()
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(
                request,
                'Your message has been sent successfully!'
            )
            return redirect('contact')
        else:
            messages.error(
                request,
                'Please fill in all required fields correctly.'
            )
    return render(request, 'classreg/contact.html', {'form':f})

def news(request):
    return render(request, 'classreg/news.html')

def started(request):
    return render(request, 'classreg/reg.html')


def p_registerview(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['Email'],
                    password=form.cleaned_data['password'],
                )
                
                parent = form.save(commit=False)
                parent.user = user
                parent.save()

                parent.students.set(
                    form.cleaned_data['students']
                )

            # Automatically log in the newly registered parent.
            login(request, user)

            return redirect('parent_dashboard')

    else:
        form = ParentForm()

    return render(
        request,
        'registration/p_reg.html',
        {'form': form}
    )


def s_registerview(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data.get('Email', ''),
                    password=form.cleaned_data['password'],
                )

                student = form.save(commit=False)
                student.user = user
                student.save()

            login(request, user)
            return redirect('student_dashboard')

    else:
        form = StudentForm()

    return render(
        request,
        'registration/s_reg.html',
        {'form': form}
    )



def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)


@login_required
@user_passes_test(is_admin)
def dashboardview(request):

    # Students
    students = Student.objects.all().order_by('-id')

    # Parents and their linked students
    parents = Parent.objects.prefetch_related(
        'students'
    ).all().order_by('id')

    # All available classes
    classes = RegisteredClass.objects.all().order_by('id')

    # Student class requests and their statuses
    enrollments = ClassEnrollment.objects.select_related(
        'student',
        'registered_class'
    ).all().order_by('-registered_on')

    # Pending class requests
    pending_requests = ClassEnrollment.objects.filter(status='Pending')

    # Approved allocations
    approved_enrollments = ClassEnrollment.objects.filter(status='Approved')

    # Contact messages
    contacts = Contact.objects.all().order_by('-id')

    context = {
        'students': students,
        'parents': parents,
        'classes': classes,
        'enrollments': enrollments,
        'pending_requests': pending_requests,
        'approved_enrollments': approved_enrollments,
        'contacts': contacts,

        # Dashboard summary cards
        'total_students': students.count(),
        'total_parents': parents.count(),
        'total_classes': classes.count(),
        'total_requests': enrollments.count(),
        'pending_count': pending_requests.count(),
        'approved_count': approved_enrollments.count(),
        'total_contacts': contacts.count(),
    }

    return render(request, 'classreg/dashboard.html', context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        role = request.POST.get("role", "")

        error = None

        if role not in ["admin", "parent", "student"]:
            error = "Please select a valid role."
        else:
            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is None:
                error = "Invalid username or password."

            elif role == "admin":
                if not user.is_superuser:
                    error = "This account is not an administrator."
                else:
                    login(request, user)
                    return redirect("dashboard")

            elif role == "parent":
                if not hasattr(user, "parent_profile"):
                    error = "No parent profile is linked to this account."
                else:
                    login(request, user)
                    return redirect("parent_dashboard")

            elif role == "student":
                if not hasattr(user, "student_profile"):
                    error = "No student profile is linked to this account."
                else:
                    login(request, user)
                    return redirect("student_dashboard")

        return render(
            request,
            "registration/login.html",
            {"error": error}
        )

    return render(request, "registration/login.html")



def logoutview(request):
    logout(request)
    return redirect('/login')


def Pdeleteview(request, id):
    Pdata = Parent.objects.get(id=id)
    Pdata.delete()
    messages.success(request, "Parent deleted successfully.")
    return redirect('/dashboard')

def Cdeleteview(request, id):
    Cdata = Contact.objects.get(id=id)
    Cdata.delete()
    messages.success(request, "Contact Message deleted successfully.")
    return redirect('/dashboard')

def Sdeleteview(request, id):
    student = get_object_or_404(Student, pk=id)

    try:
        student.delete()
        messages.success(request, "Student deleted successfully.")

    except ProtectedError:
        messages.error(
            request,
            "Unable to delete this student because they have existing "
            "class enrollments. Please resolve the enrollment records first."
        )

    # Replace this with your existing student-list page URL name.
    return redirect("/dashboard")



def classdeleteview(request, id):
    data = RegisteredClass.objects.get(id=id)
    name = data.name
    data.delete()
    messages.success(request, f'Class "{name}" deleted successfully.')
    return redirect('/dashboard')

@login_required
def student_dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        return render(
            request,
            'classreg/student_dashboard.html',
            {
                'error': 'No student profile is linked to this account.'
            }
        )

    # Get all enrollment records for the logged-in student.
    enrollments = (
        ClassEnrollment.objects
        .filter(student=student)
        .select_related('registered_class')
        .order_by('-registered_on')
    )

    # Map each class to its current enrollment status.
    enrollment_status_by_class = {}

    for enrollment in enrollments:
        class_id = enrollment.registered_class_id

        # Preserve the latest status for each class.
        if class_id not in enrollment_status_by_class:
            enrollment_status_by_class[class_id] = enrollment.status

    # Display ALL active classes, regardless of enrollment status.
    available_classes = RegisteredClass.objects.filter(
        is_active=True
    ).order_by('name')

    # Attach each class's enrollment status for the template.
    for class_item in available_classes:
        class_item.enrollment_status = enrollment_status_by_class.get(
            class_item.pk,
            ''
        )

    context = {
        'student': student,
        'enrollments': enrollments,
        'available_classes': available_classes,
        'total_classes': enrollments.count(),
        'approved_classes': enrollments.filter(
            status='Approved'
        ).count(),
        'pending_classes': enrollments.filter(
            status='Pending'
        ).count(),
        'rejected_classes': enrollments.filter(
            status='Rejected'
        ).count(),
    }

    return render(
        request,
        'classreg/student_dashboard.html',
        context
    )





@login_required
def parent_dashboard(request):
    try:
        parent = Parent.objects.get(user=request.user)
    except Parent.DoesNotExist:
        return redirect('login')

    students = parent.students.all().order_by('Name')

    student_data = []
    total_enrollments = 0
    pending_enrollments = 0

    for student in students:
        enrollments = (
            ClassEnrollment.objects
            .filter(student=student)
            .select_related('registered_class')
            .order_by('-registered_on')
        )

        total_enrollments += enrollments.count()
        pending_enrollments += enrollments.filter(
            status='Pending'
        ).count()

        student_data.append({
            'student': student,
            'enrollments': enrollments,
        })

    context = {
        'parent': parent,
        'student_data': student_data,
        'total_students': students.count(),
        'total_enrollments': total_enrollments,
        'pending_enrollments': pending_enrollments,
    }

    return render(
        request,
        'classreg/parent_dashboard.html',
        context
    )
    
    

@login_required
@user_passes_test(is_admin)
def class_create(request):

    if request.method == "POST":
        form = RegisteredClassForm(request.POST)

        if form.is_valid():
            registered_class = form.save()

            messages.success(
                request,
                f'"{registered_class.name}" Class was created successfully.'
            )

            return redirect('/dashboard')

        messages.error(
            request,
            "Please correct the errors highlighted below."
        )

    else:
        form = RegisteredClassForm()

    return render(
        request,
        'classreg/class_create.html',
        {'form': form}
    )


@login_required
def parent_edit_profile(request):
    try:
        parent = request.user.parent_profile
    except Parent.DoesNotExist:
        return redirect("user_login")

    password_form = PasswordChangeForm(user=request.user)

    # Apply Bootstrap styling to the password fields.
    for field in password_form.fields.values():
        field.widget.attrs.update({
            "class": "form-control",
            "autocomplete": "current-password"
            if field == password_form.fields.get("old_password")
            else "new-password",
        })

    if request.method == "POST":

        # Handle password change separately from profile editing.
        if request.POST.get("action") == "change_password":
            password_form = PasswordChangeForm(
                user=request.user,
                data=request.POST
            )

            for name, field in password_form.fields.items():
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["autocomplete"] = (
                    "current-password"
                    if name == "old_password"
                    else "new-password"
                )

            form = ParentProfileForm(instance=parent)

            if password_form.is_valid():
                user = password_form.save()

                # Keep the parent logged in after changing the password.
                update_session_auth_hash(request, user)

                messages.success(
                    request,
                    "Your password was changed successfully."
                )
                return redirect("parent_edit_profile")

        else:
            form = ParentProfileForm(
                request.POST,
                instance=parent
            )

            if form.is_valid():
                form.save()

                messages.success(
                    request,
                    "Your profile was updated successfully."
                )
                return redirect("parent_edit_profile")

    else:
        form = ParentProfileForm(instance=parent)

    return render(
        request,
        "classreg/parent_edit_profile.html",
        {
            "form": form,
            "parent": parent,
            "password_form": password_form,
        }
    )

@login_required
def student_edit_profile(request):
    try:
        student = request.user.student_profile
    except Student.DoesNotExist:
        return redirect("user_login")

    password_form = PasswordChangeForm(user=request.user)

    # Apply Bootstrap styling to the password fields.
    for field in password_form.fields.values():
        field.widget.attrs.update({
            "class": "form-control",
            "autocomplete": "current-password"
            if field == password_form.fields.get("old_password")
            else "new-password",
        })

    if request.method == "POST":

        # Handle password change separately from profile editing.
        if request.POST.get("action") == "change_password":
            password_form = PasswordChangeForm(
                user=request.user,
                data=request.POST
            )

            for name, field in password_form.fields.items():
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["autocomplete"] = (
                    "current-password"
                    if name == "old_password"
                    else "new-password"
                )

            form = StudentProfileForm(instance=student)

            if password_form.is_valid():
                user = password_form.save()

                # Keep the parent logged in after changing the password.
                update_session_auth_hash(request, user)

                messages.success(
                    request,
                    "Your password was changed successfully."
                )
                return redirect("student_dashboard")

        else:
            form = StudentProfileForm(
                request.POST,
                instance=student
            )

            if form.is_valid():
                form.save()

                messages.success(
                    request,
                    "Your profile was updated successfully."
                )
                return redirect("student_dashboard")

    else:
        form = StudentProfileForm(instance=student)

    return render(
        request,
        "classreg/student_edit_profile.html",
        {
            "form": form,
            "student": student,
            "password_form": password_form,
        }
    )



@login_required
@user_passes_test(is_admin)
def Seditview(request, id):
    student = get_object_or_404(Student, id=id)

    enrollments = ClassEnrollment.objects.filter(
        student=student
    ).select_related(
        'registered_class'
    ).order_by('-registered_on')

    if request.method == "POST":
        student_id = request.POST.get("Student_ID", "").strip()
        name = request.POST.get("Name", "").strip()
        dob_text = request.POST.get("Date_of_Birth", "")
        gender = request.POST.get("Gender", "")
        email = request.POST.get("Email", "").strip()
        phone = request.POST.get("Phone", "").strip()
        is_active = request.POST.get("Is_Active") == "True"

        if not all([
            student_id, name, dob_text,
            gender, email, phone
        ]):
            messages.error(
                request,
                "Please complete all required fields."
            )

        else:
            try:
                dob = date.fromisoformat(dob_text)

                student.Student_ID = student_id
                student.Name = name
                student.Date_of_Birth = dob
                student.Gender = gender
                student.Email = email
                student.Phone = phone
                student.Is_Active = is_active

                student.save()

                messages.success(
                    request,
                    "Student details updated successfully."
                )
                return redirect("dashboard")

            except ValueError:
                messages.error(
                    request,
                    "Please enter a valid date of birth."
                )

    return render(
        request,
        "classreg/sedit.html",
        {
            "student": student,
            "enrollments": enrollments,
        }
    )




@login_required
@require_POST
def request_enrollment(request, class_id):
    student = get_object_or_404(Student, user=request.user)

    registered_class = get_object_or_404(
        RegisteredClass,
        pk=class_id,
        is_active=True
    )

    enrollment, created = ClassEnrollment.objects.get_or_create(
        student=student,
        registered_class=registered_class,
        defaults={"status": "Pending"},
    )

    if created:
        messages.success(
            request,
            "Your enrollment request has been submitted."
        )

    elif enrollment.status == "Approved":
        messages.info(request, "You are already enrolled in this class.")

    elif enrollment.status == "Pending":
        messages.info(
            request,
            "Your enrollment request is already pending."
        )

    elif enrollment.status == "Rejected":
        enrollment.status = "Pending"
        enrollment.save(update_fields=["status"])
        messages.success(
            request,
            "Your enrollment request has been submitted again."
        )

    else:
        messages.error(
            request,
            "This enrollment has an unrecognized status."
        )

    return redirect("student_dashboard")




def is_classhub_admin(user):
    return user.is_authenticated and (
        user.is_staff or user.is_superuser
    )

@login_required
@user_passes_test(is_classhub_admin)
@require_POST
def update_enrollment_status(request, enrollment_id):
    enrollment = ClassEnrollment.objects.get(pk=enrollment_id)

    new_status = request.POST.get("status")

    if new_status not in ("Approved", "Rejected"):
        messages.error(request, "Invalid enrollment status.")
        return redirect("dashboard")

    enrollment.status = new_status
    enrollment.save(update_fields=["status"])

    messages.success(
        request,
        f'Enrollment for "{enrollment.student.Name}" '
        f'was {new_status.lower()}.',
    )

    if enrollment.status != "Pending":
        return redirect("dashboard")
    
    return redirect("dashboard")




@login_required
@require_POST
def delete_enrollment(request, enrollment_id):
    student = get_object_or_404(
        Student,
        user=request.user
    )

    enrollment = get_object_or_404(
        ClassEnrollment,
        pk=enrollment_id,
        student=student,
        status__in=['Pending', 'Rejected']
    )

    class_name = enrollment.registered_class.name

    enrollment.delete()

    messages.success(
        request,
        f'Your enrollment request for "{class_name}" was deleted successfully.'
    )

    return redirect('student_dashboard')



logger = logging.getLogger(__name__)

@api_view(["POST"])
def rag_chat(request):
    question = request.data.get("message", "").strip()

    if not question:
        return Response(
            {"error": "Please enter a question."},
            status=400,
        )

    if len(question) > 2000:
        return Response(
            {"error": "Please keep your question under 2000 characters."},
            status=400,
        )

    try:
        answer = get_classhub_response(question)

        if not answer:
            answer = (
                "I'm unable to provide an answer right now. "
                "Please contact the ClassHub administrator."
            )

        return Response({
            "user_message": question,
            "ai_response": answer,
        })

    except Exception:
        logger.exception("ClassHub assistant request failed")

        return Response(
            {
                "error": (
                    "The assistant is temporarily unavailable. "
                    "Please try again later."
                )
            },
            status=503,
        )
