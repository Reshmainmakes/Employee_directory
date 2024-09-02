from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email_address', 'department', 'dob','agreement_document', 'additional_document')
    search_fields = ('name', 'phone_number', 'email_address', 'department')
    list_filter = ('department',)
    readonly_fields = ('agreement_document', 'additional_document')

    fieldsets = (
        (None, {
            'fields': ('name', 'phone_number', 'email_address', 'dob', 'department')
        }),
        ('Addresses', {
            'fields': ('home_address', 'work_address')
        }),
        ('Contacts', {
            'fields': ('emergency_contact',)
        }),
        ('Documents', {
            'fields': ('agreement_document', 'additional_document')
        }),
    )

admin.site.register(Employee, EmployeeAdmin)
