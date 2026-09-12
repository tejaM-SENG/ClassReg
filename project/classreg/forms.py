from django import forms
from classreg.models import Parent, Contact
from django.contrib.auth.models import User

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'
        
        widgets = {
            'Name': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter your name'
            }),

            'Phone': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter phone number'
            }),

            'Email': forms.EmailInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter email address'
            }),

            'Student_Name': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter student name'
            }),

            'Message': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Type your message here',
                'rows': 4
            }),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
        widgets = {
            'Name': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter your name'
            }),

            'Phone': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter phone number'
            }),

            'Email': forms.EmailInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter email address'
            }),

            'Message': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Type your message here',
                'rows': 4
            }),
        }