from django.db import models


# Create your models here.
#Define las clases en este archivo;
class ErrorLog(models.Model):
    codigo= models.CharField(max_length=10)
    mensaje= models.TextField()
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Codigo: {codigo} - mensaje: {mensaje} "