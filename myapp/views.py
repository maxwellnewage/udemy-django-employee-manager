from django.shortcuts import render
from myapp.models import Person, Company, Employee


def home(request):
    return render(request, 'home.html', {
        'title': 'Gestor de Empleados',
        'person_counter': Person.objects.count(),
        'company_counter': Company.objects.count(),
        'employee_counter': Employee.objects.count(),
    })
