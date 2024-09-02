# Generated by Django 4.2.15 on 2024-09-01 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email_address', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('department', models.CharField(max_length=100)),
                ('emergency_contact', models.CharField(max_length=15)),
                ('home_address', models.TextField()),
                ('work_address', models.TextField()),
                ('agreement_document', models.FileField(blank=True, null=True, upload_to='agreements/')),
                ('additional_document', models.FileField(blank=True, null=True, upload_to='documents/')),
            ],
        ),
    ]