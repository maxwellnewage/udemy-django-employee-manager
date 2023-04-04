from django.db.models import Q
from django.shortcuts import render, redirect
from myapp.forms import PersonForm
from myapp.models import Person


def read(request):
    term = request.GET.get('term') if request.GET.get('term') is not None else ''
    person_list = Person.objects.filter(Q(firstname__icontains=term) | Q(lastname__icontains=term))

    return render(request, 'persons.html', {
        'title': 'Lista de Personas',
        'person_list': person_list,
        'search_title': 'Busca una persona...'
    })


def create(request):
    form = PersonForm()

    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('persons_view')

    return render(request, 'entity_form.html', {
        'title': 'Crear nueva Persona',
        'form': form
    })


def update(request, person_id):
    person = Person.objects.get(id=person_id)
    form = PersonForm(instance=person)

    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('persons_view')

    return render(request, 'entity_form.html', {
        'title': f'Edición de {person}',
        'form': form
    })


def delete(request, person_id):
    person = Person.objects.get(id=person_id)

    if request.method == "POST":
        person.delete()
        return redirect('persons_view')

    return render(request, 'entity_delete.html', {'entity': person})
