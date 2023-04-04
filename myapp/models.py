from django.db import models


class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    passport = models.IntegerField(unique=True)
    email = models.EmailField(null=True, blank=True)
    height = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    portfolio = models.URLField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Company(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.person} | {self.company} | ${self.salary}"
