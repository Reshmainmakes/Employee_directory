from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm

from datetime import datetime
from django.shortcuts import render
from .models import Employee

def login_option(request):
    today = datetime.now().date()
    birthday_employees = Employee.objects.filter(dob__month=today.month, dob__day=today.day)
    birthday_message = None

    if birthday_employees.exists():
        birthday_message = "Happy Birthday to: " + ", ".join([e.name for e in birthday_employees])

    return render(request, 'directory/login_option.html', {'birthday_message': birthday_message})

from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def manager_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee_list')
        else:
            return render(request, 'directory/manager_login.html', {'error': 'Invalid credentials'})
    return render(request, 'directory/manager_login.html')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'directory/employee_list.html', {'employees': employees})

@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'directory/add_employee.html', {'form': form})


def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        file = request.FILES.get('additional_document')
        if file:
            employee.additional_document = file
            employee.save()
            return redirect('employee_detail', pk=pk)
    return render(request, 'directory/employee_detail.html', {'employee': employee})

def employee_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            employee = Employee.objects.get(name=username, phone_number=password)
            return redirect('employee_detail', pk=employee.id)
        except Employee.DoesNotExist:
            return render(request, 'directory/employee_login.html', {'error': 'Invalid credentials'})
    return render(request, 'directory/employee_login.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login_option')  # Redirect to the initial login page after logout

from django.shortcuts import render, redirect, get_object_or_404
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)  # Include request.FILES here
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'directory/add_employee.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'directory/employee_confirm_delete.html', {'employee': employee})
