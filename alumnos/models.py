from django.db import models

# Create your models here.

class Alumnos (models.Model):
    nombre=models.CharField(max_length=200)
    Apellido=models.CharField(max_length=200)
    Edad=models.IntegerField()
    Matricula =models.CharField(unique=True,max_length=15)
    Correo =models.CharField(unique=True,max_length=200)