from django.contrib import admin
from .models import (
    Parent,
    Student,
    RegisteredClass,
    ClassEnrollment,
    Contact,
)


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Name',
        'Phone',
        'Email',
        'linked_students',
    )

    search_fields = (
        'Name',
        'Email',
        'Phone',
        'students__Name',
        'students__Student_ID',
    )

    filter_horizontal = ('students',)

    @admin.display(description='Linked Students')
    def linked_students(self, obj):
        return ', '.join(
            f'{student.Student_ID} - {student.Name}'
            for student in obj.students.all()
        ) or 'No students linked'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'Student_ID',
        'Name',
        'Email',
        'Is_Active',
    )

    list_filter = (
        'Gender',
        'Is_Active',
    )

    search_fields = (
        'Student_ID',
        'Name',
        'Email',
        'user__username',
    )


class EnrollmentInline(admin.TabularInline):
    model = ClassEnrollment
    extra = 0


@admin.register(RegisteredClass)
class RegisteredClassAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'course',
        'instructor',
        'capacity',
        'price',
        'is_active',
    )

    list_editable = ("price", "is_active")
    list_filter = ('is_active',)
    search_fields = ('name', 'course', 'instructor')
    inlines = [EnrollmentInline]


@admin.register(ClassEnrollment)
class ClassEnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'registered_class',
        'registered_on',
        'status',
    )

    list_filter = (
        'status',
        'registered_on',
    )

    search_fields = (
        'student__Name',
        'student__Student_ID',
        'registered_class__name',
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone')
    search_fields = ('Name', 'Email', 'Phone')