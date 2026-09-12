from django.contrib import admin
from classreg.models import Parent, Contact

# Register your models here.

class ParentAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Student_Name')
    
admin.site.register(Parent, ParentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone')
    
admin.site.register(Contact, ContactAdmin)

