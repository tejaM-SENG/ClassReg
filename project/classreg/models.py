from django.db import models

# Create your models here.

class Parent(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Email = models.EmailField()
    Student_Name = models.CharField(max_length=100)
    Message = models.TextField(max_length=1000)
    
class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Email = models.EmailField()
    Message = models.CharField(max_length=1000)