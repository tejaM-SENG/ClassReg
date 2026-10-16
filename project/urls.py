"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from classreg import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', views.home, name='home'),
    path('python/', views.python),
    path('java/', views.java),
    path('django/', views.django),
    path('photos/', views.photos),
    path('videos/', views.videos),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news),
    path('started/', views.started),
    path('parent_reg/', views.p_registerview),
    path('student_reg/', views.s_registerview, name='s_registerview'),
    path('dashboard/', views.dashboardview,name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.user_login),
    path('logout/', views.logoutview),
    path('Pdelete/<int:id>/', views.Pdeleteview),
    path('Cdelete/<int:id>/', views.Cdeleteview),
    path('classdelete/<int:id>/', views.classdeleteview, name='classdelete'),
    path('Sdelete/<int:id>/', views.Sdeleteview, name='Sdelete'),
    path('Sedit/<int:id>/', views.Seditview, name='Sedit'),
    path('student-dashboard/',views.student_dashboard,name='student_dashboard'),
    path('parent-dashboard/',views.parent_dashboard,name='parent_dashboard'),
    path('parent/edit-profile/',views.parent_edit_profile,name="parent_edit_profile"),
    path('student/edit-profile/',views.student_edit_profile,name="student_edit_profile"),
    path("student/enroll/<int:class_id>/",views.request_enrollment,name="request_enrollment",),
    path('classcreate/',views.class_create, name='class_create'),
    path("enrollment/<int:enrollment_id>/status/", views.update_enrollment_status, name="update_enrollment_status",),
    path('enrollment/<int:enrollment_id>/delete/', views.delete_enrollment, name='delete_enrollment'),
    path("chat/", views.rag_chat, name='rag_chat'),
]

