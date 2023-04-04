from django.shortcuts import render, redirect

from myapp.forms import EmployeeForm
from myapp.models import Employee

from django.db.models import Q


def read(request):
    term = request.GET.get('term') if request.GET.get('term') is not None else ''
    employees = Employee.objects.filter(
        Q(person__firstname__icontains=term) |
        Q(person__lastname__icontains=term) |
        Q(company__name__icontains=term)
    )

    return render(request, 'employees.html', {
        'title': 'Lista de Empleados',
        'employees': employees,
        'search_title': 'Busca un empleado...'
    })


def create(request):
    form = EmployeeForm()

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees_view')

    return render(request, 'entity_form.html', {
        'title': 'Crear nuevo Empleado',
        'form': form
    })


def update(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    form = EmployeeForm(instance=employee)

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees_view')

    return render(request, 'entity_form.html', {
        'title': f'Edición de {employee}',
        'form': form
    })


def delete(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    if request.method == "POST":
        employee.delete()
        return redirect('employees_view')

    return render(request, 'entity_delete.html', {'entity': employee})
