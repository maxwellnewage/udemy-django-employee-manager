# Generated by Django 4.1.7 on 2023-03-15 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_roles_rol'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rol',
        ),
    ]
