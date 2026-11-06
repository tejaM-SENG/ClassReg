# ClassHub – Class Registration Management System

ClassHub is a web-based Class Registration Management System developed using Python and Django. The application simplifies the class enrollment process by providing dedicated dashboards for administrators, parents, and students, along with an enrollment approval workflow.

## 🚀 Live Demo

**Live Application:**  https://classreg-95wo.onrender.com/   

**GitHub Repository:**  https://github.com/tejaM-SENG/ClassHub/

## 📌 Project Overview

ClassHub is designed to streamline academic class registration and enrollment management.

The platform allows parents to manage their students' information and register them for available classes. Administrators can manage class offerings, review enrollment requests, and approve or reject registrations through a centralized dashboard.

## ✨ Key Features

- **Admin Dashboard:** Centralized dashboard for managing registration activities.
- **Parent Dashboard:** Dedicated interface for parents to manage their students.
- **Student Management:** Maintain student information and profiles.
- **Class Management:** Manage available classes and registration information.
- **Class Enrollment:** Parents can enroll their students in available classes.
- **Enrollment Approval:** Administrators can review and approve enrollment requests.
- **Enrollment Rejection:** Administrators can reject enrollment requests.
- **Enrollment Status Tracking:** Monitor pending, approved, and rejected applications.
- **Role-Based Access:** Separate interfaces and permissions for administrators, parents, and students.
- **Responsive UI:** Bootstrap-based interface for desktop and mobile devices.

## 👥 User Roles

### 1. Administrator
- Access the administration dashboard.
- Manage registration information.
- Review class enrollment requests.
- Approve or reject enrollment applications.
- Monitor enrollment activities.

### 2. Parent
- Access the parent dashboard.
- Manage student information.
- View available classes.
- Register students for classes.
- Track enrollment status.

### 3. Student
- Access student-related information through the application.
- View relevant registration and enrollment details according to assigned permissions.

## 🔐 Demo Login Credentials

Use the following demo accounts to explore the application.

| User Role | Username | Password |
|---|---|---|
| Admin | demo@admin | demo@1234 |
| Parent | demo@parent | pare@1234 |
| Student1 | demo@student1 | stud@1234 |
| Student2 | demo@student2 | stud@1234 |

**Note:** Replace these placeholders with actual accounts created in your deployed application. Use dedicated test accounts and sample data instead of personal credentials.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | Django |
| Frontend | HTML, CSS, JavaScript |
| UI Framework | Bootstrap 5.3.8 |
| Icons | Bootstrap Icons |
| Database | SQLite3 |
| Authentication | Django Authentication |
| Version Control | Git & GitHub |
| Deployment | Render |

## 📂 Project Structure

```text
ClassHub/
│
├── classreg/
│   ├── migrations/
│   ├── tests.py
│   ├── classhub_faqs.txt
│   ├── gemini_service.py
│   ├── middleware.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── apps.py
│   └── admin.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── classreg/
│   └── registration/
│
├── static/
│   ├── images/
│   └── css/
│
├── screenshots/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

*Note: Adjust the directory names according to your actual repository.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd ClassHub
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file for gemini_api_key.

Configure the Django secret key and other required environment-specific settings.

Do not upload actual credentials or secret keys to GitHub.

### 7. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create an Administrator Account

```bash
python manage.py createsuperuser
```

### 9. Run the Development Server

```bash
python manage.py runserver
```

Open the application:

http://127.0.0.1:8000/

## 📊 Database Models

The application uses Django models to manage registration data.

Key models include:

- **Parent:** Stores parent account and student relationships.
- **Student:** Stores student information and classes registered.
- **RegisteredClass:** Stores available class information.
- **ClassEnrollment:** Maintains student enrollment records and application status.

### Enrollment Status

| Status | Description |
|---|---|
| Pending | Enrollment request submitted and awaiting review |
| Approved | Enrollment request accepted by administrator |
| Rejected | Enrollment request declined by administrator |

## 🖥️ Application Screenshots

Add screenshots of the main application interfaces.

| Interface | Screenshot |
|---|---|
| Admin Dashboard | <img width="2842" height="1278" alt="image" src="https://github.com/user-attachments/assets/18f8372d-b48c-463d-b8a3-872e6d98e859" /><img width="2842" height="1084" alt="image" src="https://github.com/user-attachments/assets/9a8f0c54-4d17-45f8-8a4b-b07cfabb2eb4" /><img width="2858" height="892" alt="image" src="https://github.com/user-attachments/assets/8860b578-f520-437e-82cd-9cd6db2db3c3" /><img width="2848" height="1120" alt="image" src="https://github.com/user-attachments/assets/e609fea1-a1ce-4a4b-a518-a7d6d00fac08" /><img width="2842" height="1120" alt="image" src="https://github.com/user-attachments/assets/24d9e77c-3f0e-44ec-a2de-1b7379e7bb2c" /><img width="2850" height="1124" alt="image" src="https://github.com/user-attachments/assets/251151e9-40b4-42b6-be84-b5aebc3e3547" /> |
| Parent Dashboard | <img width="2852" height="1276" alt="image" src="https://github.com/user-attachments/assets/4c5563e8-f294-40e0-8cd0-de0554bfd42b" /><img width="2846" height="1100" alt="image" src="https://github.com/user-attachments/assets/bb9af111-0b8f-4432-a855-4400b35b659a" /> |
| Student Dashboard | <img width="2846" height="1228" alt="image" src="https://github.com/user-attachments/assets/2ff22807-1095-4b36-8419-8f46e6b98206" /><img width="2836" height="1122" alt="image" src="https://github.com/user-attachments/assets/5c672dd9-7b80-4fbc-b5b9-fcd4f30ee06e" /><img width="2834" height="1122" alt="image" src="https://github.com/user-attachments/assets/328ccdd7-e728-47af-bf52-8d929646d97d" /> |
| Class Registration | <img width="2838" height="1276" alt="image" src="https://github.com/user-attachments/assets/9ad1fba6-7fb3-4cee-bf7d-fd87fc1a5918" /><img width="2824" height="1280" alt="image" src="https://github.com/user-attachments/assets/92bbebca-4ed6-4011-b15c-9fe6f270d642" /> |
| Enrollment Management | <img width="2848" height="1274" alt="image" src="https://github.com/user-attachments/assets/04415fd2-0d73-4f7c-9cff-48a5e0453dda" /><img width="2844" height="1280" alt="image" src="https://github.com/user-attachments/assets/082b8cd4-5627-44b0-90e3-f93e3f7259e1" /><img width="2844" height="1284" alt="image" src="https://github.com/user-attachments/assets/2580959d-bce1-4ab3-9a8a-1a877f716984" /><img width="2840" height="1114" alt="image" src="https://github.com/user-attachments/assets/3144c613-9d57-43dc-a06e-cdad6950dda0" /> |
| Login Page | <img width="2852" height="1286" alt="image" src="https://github.com/user-attachments/assets/44b66cb9-491d-42b4-98dd-9110e66791d0" /><img width="2848" height="564" alt="image" src="https://github.com/user-attachments/assets/76bc8224-35d5-4c98-af09-b9d697332803" /> |

## ☁️ Deployment

The application is deployed using Render.

Deployment workflow:

1. Push source code to GitHub.
2. Connect the repository to Render.
3. Configure the Python environment.
4. Install dependencies using `requirements.txt`.
5. Configure environment variables.
6. Apply database migrations.
7. Configure static file handling.
8. Deploy the application.

**Live Application:** ADD_YOUR_RENDER_LIVE_URL

## 🎯 Project Objectives

- Simplify academic class registration.
- Provide a centralized enrollment management system.
- Implement role-based authentication and authorization.
- Develop an enrollment approval and rejection workflow.
- Manage parent and student relationships.
- Build responsive dashboards using Django and Bootstrap.
- Gain practical experience in full-stack web development and deployment.

## 👨‍💻 Developer

**Teja Muddangula**

Python Full-Stack Developer

- GitHub: https://github.com/tejaM-SENG
- LinkedIn: https://linkedin.com/in/teja-muddangula-38a92a218

---

*Developed as a Python Full-Stack Web Development project.*
