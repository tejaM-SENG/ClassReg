from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from decimal import Decimal

class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='student_profile'
    )

    Student_ID = models.CharField(
        max_length=20, unique=True, blank=True
    )
    Name = models.CharField(max_length=100)
    Date_of_Birth = models.DateField(null=True, blank=True)
    Gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, blank=True
    )
    Email = models.EmailField(blank=True)
    Phone = models.CharField(max_length=20, blank=True)
    Date_Registered = models.DateTimeField(auto_now_add=True)
    Is_Active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.Student_ID:
            last_student = Student.objects.order_by('-id').first()
            next_id = last_student.id + 1 if last_student else 1
            self.Student_ID = f"STU{next_id:05d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Student_ID} - {self.Name}"


class Parent(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='parent_profile'
    )

    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField()
    Address = models.TextField(blank=True)
    Date_Registered = models.DateTimeField(auto_now_add=True)

    # One parent can select multiple students.
    # A student can also be linked to multiple parents.
    students = models.ManyToManyField(
        Student,
        related_name='parents',
        blank=True
    )

    def __str__(self):
        return self.Name


class RegisteredClass(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    schedule = models.CharField(max_length=150, blank=True)
    capacity = models.PositiveIntegerField(default=30)
    is_active = models.BooleanField(default=True)
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0.00"))],
        )
    
    students = models.ManyToManyField(
        Student,
        through='ClassEnrollment',
        related_name='registered_classes',
        blank=True
    )

    def __str__(self):
        return self.name


class ClassEnrollment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        related_name='enrollments'
    )

    registered_class = models.ForeignKey(
        RegisteredClass,
        on_delete=models.PROTECT,
        related_name='enrollments'
    )

    registered_on = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    # Optional progress percentage for the parent/student dashboards.
    progress = models.PositiveSmallIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'registered_class'],
                name='unique_student_class_enrollment'
            )
        ]

    def __str__(self):
        return f"{self.student.Name} - {self.registered_class.name}"


class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField()
    Message = models.CharField(max_length=1000)
    contacted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

