import re
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError # Adjust if your validators are elsewhere

from .models import (
    Parent,
    Student,
    RegisteredClass,
    ClassEnrollment,
    Contact,
)

User = get_user_model()


def validate_name(value):
    if not re.fullmatch(r"[A-Za-z ]+", value.strip()):
        raise forms.ValidationError(
            "Name must contain only alphabets and spaces."
        )


def validate_phone(value):
    if not re.fullmatch(r"[0-9]{10}", value):
        raise forms.ValidationError(
            "Phone number must contain only 10 values or numeric digits."
        )


class ParentForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Choose a username',
            'autocomplete': 'username',
        }),
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create a password',
            'autocomplete': 'new-password',
        }),
        help_text=(
            "Your password can't be too similar to your personal information. "
            "It must contain at least 8 characters, can't be commonly used, "
            "and can't be entirely numeric."
        ),
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter your password',
            'autocomplete': 'new-password',
        }),
    )

    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.filter(Is_Active=True),
        required=True,
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'form-check-input'}
        ),
        label='Select Your Student(s)',
    )

    Name = forms.CharField(
        validators=[validate_name],
        error_messages={
            'required': 'Please enter a valid name.'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your full name',
        }),
    )

    Phone = forms.CharField(
        validators=[validate_phone],
        error_messages={
            'required': 'Please enter a valid phone number.'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter phone number',
        }),
    )

    class Meta:
        model = Parent
        fields = ['Name', 'Phone', 'Email', 'Address']

        widgets = {
            'Email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address',
            }),
            'Address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address',
                'rows': 3,
            }),
        }

    def clean_username(self):
        username = self.cleaned_data['username'].strip()

        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                'This username is already taken.'
            )

        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        # Django applies the configured password validators.
        validate_password(password)

        return password

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password:
            temp_user = User(
            username=cleaned_data.get('username', ''),
            email=cleaned_data.get('Email', ''),
        )

        try:
            validate_password(password, user=temp_user)
        except ValidationError as error:
            self.add_error('password', error)

        if password and confirm_password and password != confirm_password:
            self.add_error(
                'confirm_password',
                'The passwords do not match.'
            )

        return cleaned_data



class StudentForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Choose a username',
            'autocomplete': 'username',
        }),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create a password',
            'autocomplete': 'new-password',
        }),
    )

    Name = forms.CharField(
        validators=[validate_name],
        error_messages={
            "required": "Please enter valid name."
        }
    )

    Phone = forms.CharField(
        validators=[validate_phone],
        error_messages={
            "required": "Please enter valid phone number."
        }
    )
    
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter your password',
            'autocomplete': 'new-password',
        }),
    )


    class Meta:
        model = Student
        fields = [
            'Name',
            'Date_of_Birth',
            'Gender',
            'Email',
            'Phone',
        ]

        widgets = {
            'Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name',
            }),
            'Date_of_Birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'Gender': forms.Select(attrs={
                'class': 'form-select',
            }),
            'Email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address',
            }),
            'Phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number',
            }),
        }

    def clean_username(self):
        username = self.cleaned_data['username'].strip()

        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                'This username is already taken.'
            )

        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        # Django applies the configured password validators.
        validate_password(password)

        return password

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password:
            temp_user = User(
            username=cleaned_data.get('username', ''),
            email=cleaned_data.get('Email', ''),
        )

        try:
            validate_password(password, user=temp_user)
        except ValidationError as error:
            self.add_error('password', error)

        if password and confirm_password and password != confirm_password:
            self.add_error(
                'confirm_password',
                'The passwords do not match.'
            )

        return cleaned_data


class RegisteredClassForm(forms.ModelForm):
    class Meta:
        model = RegisteredClass

        fields = [
            'name',
            'course',
            'instructor',
            'description',
            'schedule',
            'capacity',
            'price',
            'is_active',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Python Full Stack Development',
            }),
            'course': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Software Development',
            }),
            'instructor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter instructor name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the class, learning objectives, and topics...',
                'rows': 4,
            }),
            'schedule': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Monday and Wednesday, 10 AM',
            }),
            'capacity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'placeholder': '30',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'step': '0.01',
                'placeholder': '0.00',
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class ClassEnrollmentForm(forms.ModelForm):
    class Meta:
        model = ClassEnrollment

        fields = [
            'student',
            'registered_class',
            'status',
        ]

        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-select',
            }),
            'registered_class': forms.Select(attrs={
                'class': 'form-select',
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
        }


class ContactForm(forms.ModelForm):
    Name = forms.CharField(
        widget=forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter your name',
            }),
        validators=[validate_name],
        error_messages={
            "required": "Please enter valid name."
            }
        )

    Phone = forms.CharField(
        validators=[validate_phone],
        error_messages={
            "required": "Please enter valid phone number."
            },
        widget=forms.TextInput(attrs={
            'class': 'form-control w-100',
            'placeholder': 'Enter phone number',
            })
        )
    
    class Meta:
        model = Contact
        fields = '__all__'
        
        
        widgets = {
            'Email': forms.EmailInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter email address',
            }),
            'Message': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Type your message here',
                'rows': 4,
            }),
        }

        

class ParentProfileForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ["Name", "Email", "Phone", "Address"]

        widgets = {
            "Name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your full name"
            }),
            "Email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email address"
            }),
            "Phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your phone number"
            }),
            "Address": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter your address",
                "rows": 3
            }),
        }
        
        

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["Name", "Email", "Phone"]

        widgets = {
            "Name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your full name"
            }),
            "Email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email address"
            }),
            "Phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your phone number"
            }),
        }