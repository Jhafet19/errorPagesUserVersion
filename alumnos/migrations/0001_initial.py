# Generated by Django 5.1.4 on 2025-02-24 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('Apellido', models.CharField(max_length=200)),
                ('Edad', models.IntegerField()),
                ('Matricula', models.CharField(max_length=15, unique=True)),
                ('Correo', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
