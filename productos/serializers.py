# UNA clase que toma un modelo 
from rest_framework import  serializers
from .models import Producto

class ProductoSerializar(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields='__all__'
        
    