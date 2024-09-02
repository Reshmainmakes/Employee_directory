from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    dob = models.DateField()
    department = models.CharField(max_length=100)
    emergency_contact = models.CharField(max_length=15)
    home_address = models.TextField()
    work_address = models.TextField()
    agreement_document = models.FileField(upload_to='agreements/', blank=True, null=True)
    additional_document = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.name
