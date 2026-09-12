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
    path('/', views.home),
    path('python/', views.python),
    path('java/', views.java),
    path('django/', views.django),
    path('photos/', views.photos),
    path('videos/', views.videos),
    path('contact/', views.contact),
    path('news/', views.news),
    path('register/', views.registerview),
    path('dashboard/', views.dashboardview),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.loginview),
    path('logout/', views.logoutview),
    path('Pdelete/<int:id>/', views.Pdeleteview),
    path('Cdelete/<int:id>/', views.Cdeleteview),
]
