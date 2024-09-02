from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_option, name='login_option'),
    path('manager-login/', views.manager_login, name='manager_login'),
    path('employee-list/', views.employee_list, name='employee_list'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('employee-detail/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employee-login/', views.employee_login, name='employee_login'),
path('accounts/login/', views.manager_login, name='manager_login'),
path('logout/', views.logout_view, name='logout'),
path('update/<int:pk>/', views.employee_update, name='employee_update'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
]