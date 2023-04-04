from django.urls import path

from .custom_views import views_person, views_company, views_employee
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('persons/', views_person.read, name='persons_view'),
    path('persons/create', views_person.create, name='person_create'),
    path('persons/update/<str:person_id>', views_person.update, name='person_update'),
    path('persons/delete/<str:person_id>', views_person.delete, name='person_delete'),

    path('companies/', views_company.read, name='companies_view'),
    path('companies/create', views_company.create, name='company_create'),
    path('companies/update/<str:company_id>', views_company.update, name='company_update'),
    path('companies/delete/<str:company_id>', views_company.delete, name='company_delete'),

    path('employees/', views_employee.read, name='employees_view'),
    path('employees/create', views_employee.create, name='employee_create'),
    path('employees/update/<str:employee_id>', views_employee.update, name='employee_update'),
    path('employees/delete/<str:employee_id>', views_employee.delete, name='employee_delete'),
]
