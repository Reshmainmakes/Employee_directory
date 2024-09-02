from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name', 'phone_number', 'email_address', 'dob',
            'department', 'emergency_contact', 'home_address',
            'work_address', 'agreement_document'
        ]

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }