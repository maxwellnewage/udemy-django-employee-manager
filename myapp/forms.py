from django.forms import ModelForm
from .models import Person, Company, Employee


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
