from django.shortcuts import render
from .models import Producto
from .serializers import ProductoSerializar
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .forms import productoForm

class ProductoViewSet(viewsets.ModelViewSet):
    queryset=Producto.objects.all()
    serializer_class= ProductoSerializar
    renderer_classes=[JSONRenderer]
    #http_method_names= ['GET','POST']

def agregar_producto(request):
    form = productoForm
    return render(request,'agregar.html',{'form':form})
