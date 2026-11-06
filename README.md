# ClassReg – Class Registration Management System

ClassReg is a web-based Class Registration Management System developed using Python and Django. The application simplifies the class enrollment process by providing dedicated dashboards for administrators, parents, and students, along with an enrollment approval workflow.

## 🚀 Live Demo

**Live Application:**  https://classreg-95wo.onrender.com/   

**GitHub Repository:**  https://github.com/tejaM-SENG/ClassReg/

## 📌 Project Overview

ClassReg is designed to streamline academic class registration and enrollment management.

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
ClassReg/
│
├── classreg/
│   ├── migrations/
│   ├── tests.py
│   ├── classreg_faqs.txt
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
cd ClassReg
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
| Admin Dashboard | <img width="2838" height="1256" alt="image" src="https://github.com/user-attachments/assets/b8813909-6ac9-415e-ae66-0b475c8c5ef6" /><img width="2830" height="1070" alt="image" src="https://github.com/user-attachments/assets/04166bb4-1670-439d-b99e-fe401aab640f" /><img width="2840" height="1066" alt="image" src="https://github.com/user-attachments/assets/916957bc-a77b-4013-99c4-3fe1eeba51e3" /><img width="2840" height="1118" alt="image" src="https://github.com/user-attachments/assets/356b5306-9d91-4cde-b1e5-e5ea9f039722" /><img width="2842" height="1068" alt="image" src="https://github.com/user-attachments/assets/2c2729d3-85c8-4f49-8b14-cc11e4c38fea" /><img width="2838" height="1070" alt="image" src="https://github.com/user-attachments/assets/8b45316f-2213-444f-9474-31f7118b27bc" /><img width="2840" height="1044" alt="image" src="https://github.com/user-attachments/assets/c535dfc7-805f-497d-9512-2e695654207d" /> |
| Parent Dashboard | <img width="2844" height="1278" alt="image" src="https://github.com/user-attachments/assets/f7a2eeaf-4bbb-4acf-a558-fe61313a4951" /><img width="2850" height="1116" alt="image" src="https://github.com/user-attachments/assets/4f3453b0-08df-4b68-a504-0f0d92698542" /> |
| Student Dashboard | <img width="2834" height="1214" alt="image" src="https://github.com/user-attachments/assets/c4fe48ff-eaf6-4109-86cf-e4032420764a" /><img width="2844" height="1128" alt="image" src="https://github.com/user-attachments/assets/20b6a3db-484d-4229-9f8b-a8b091fb5165" /><img width="2842" height="1120" alt="image" src="https://github.com/user-attachments/assets/bd092b04-531b-44c7-a0f7-b7956795a118" /> |
| Class Registration | <img width="2844" height="1128" alt="image" src="https://github.com/user-attachments/assets/0ac94936-6554-4d06-956d-6290a5b1f9fd" /><img width="2844" height="1274" alt="image" src="https://github.com/user-attachments/assets/b83a0253-4d97-4e1b-976c-dc4fe9854f1e" /> |
| Enrollment Management | <img width="2842" height="1268" alt="image" src="https://github.com/user-attachments/assets/6420de92-3fd6-4b7d-83db-02e22ff19f79" /><img width="2844" height="626" alt="image" src="https://github.com/user-attachments/assets/ef8d70ef-2983-4694-9ca1-e4ebfe2dcc53" /><img width="2844" height="1276" alt="image" src="https://github.com/user-attachments/assets/f873d169-9453-4157-b880-717439aa634d" /><img width="2842" height="986" alt="image" src="https://github.com/user-attachments/assets/9fd87551-70d1-4fef-9e33-8026b090e84a" /> |
| Login Page | <img width="2850" height="1278" alt="image" src="https://github.com/user-attachments/assets/9d4d151f-26cd-4fe2-bcfe-0a630e20a0d8" /><img width="2842" height="998" alt="image" src="https://github.com/user-attachments/assets/c2cae7ab-7122-4c6a-a0a4-e4c38c3bb75a" /> |

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
