from django.shortcuts import render, redirect

from myapp.forms import CompanyForm
from myapp.models import Company


def read(request):
    term = request.GET.get('term') if request.GET.get('term') is not None else ''
    companies = Company.objects.filter(name__icontains=term)

    return render(request, 'companies.html', {
        'title': 'Lista de Compañías',
        'companies': companies,
        'search_title': 'Busca una compañía...'
    })


def create(request):
    form = CompanyForm()

    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('companies_view')

    return render(request, 'entity_form.html', {
        'title': 'Crear nueva Compañía',
        'form': form
    })


def update(request, company_id):
    company = Company.objects.get(id=company_id)
    form = CompanyForm(instance=company)

    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('companies_view')

    return render(request, 'entity_form.html', {
        'title': f'Edición de {company}',
        'form': form
    })


def delete(request, company_id):
    company = Company.objects.get(id=company_id)

    if request.method == "POST":
        company.delete()
        return redirect('companies_view')

    return render(request, 'entity_delete.html', {'entity': company})

