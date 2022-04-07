# Generated by Django 3.1.7 on 2022-04-06 12:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre del aplicante')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido del aplicante')),
                ('dni', models.IntegerField(unique=True, verbose_name='Nº de documento (DNI)')),
                ('gender', models.CharField(max_length=50, verbose_name='Genero del aplicante')),
                ('email', models.EmailField(max_length=254, verbose_name='Email de contacto')),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('status', models.BooleanField(default=False, verbose_name='Aprobado por la API')),
            ],
            options={
                'verbose_name': 'Aplicante',
                'verbose_name_plural': 'Aplicantes',
            },
        ),
        migrations.CreateModel(
            name='ApiQueries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('status_api', models.IntegerField(verbose_name='Status code de la respuesta')),
                ('response_api', models.CharField(max_length=100, verbose_name='Respuesta de la API')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.applicant', verbose_name='Aplicante')),
            ],
            options={
                'verbose_name': 'Registro de consultas',
                'verbose_name_plural': 'Registros de consultas',
            },
        ),
    ]
