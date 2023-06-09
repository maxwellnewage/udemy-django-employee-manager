# Generated by Django 4.1.7 on 2023-03-15 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_delete_employee_delete_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.company')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.person')),
            ],
        ),
    ]
