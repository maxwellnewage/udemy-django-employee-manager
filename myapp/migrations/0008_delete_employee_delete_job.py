# Generated by Django 4.1.7 on 2023-03-15 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_job_employee'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
