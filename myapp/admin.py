from django.contrib import admin
from .models import Person, Company, Employee

# Register your models here.
admin.site.register([Person, Company, Employee])
