# UNA clase que toma un modelo 
from rest_framework import  serializers
from .models import Alumnos

class AlumnosSerializar(serializers.ModelSerializer):
    class Meta:
        model=Alumnos
        fields='__all__'
        
    