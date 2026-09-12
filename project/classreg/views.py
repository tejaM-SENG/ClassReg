from django.shortcuts import render, redirect
from classreg.models import Parent, Contact
from classreg.forms import ParentForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request, 'classreg/home.html')

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
            return redirect('/home')
    return render(request, 'classreg/contact.html', {'form':f})

def news(request):
    return render(request, 'classreg/news.html')

def registerview(request):
    f=ParentForm()
    if request.method == 'POST':
        f = ParentForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/home')
    return render(request, 'registration/register.html', {'form':f})

@login_required
def dashboardview(request):
    Pdata = Parent.objects.all()
    Cdata = Contact.objects.all()
    return render(request, 'classreg/dashboard.html', {'p': Pdata, 'c': Cdata})

def loginview(request):
    return render(request, 'registration/login.html')

def logoutview(request):
    logout(request)
    return redirect('/login')


def Pdeleteview(request, id):
    Pdata = Parent.objects.get(id=id)
    Pdata.delete()
    return redirect('/dashboard')

def Cdeleteview(request, id):
    Cdata = Contact.objects.get(id=id)
    Cdata.delete()
    return redirect('/dashboard')