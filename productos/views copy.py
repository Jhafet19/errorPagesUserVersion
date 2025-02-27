import json
from django.shortcuts import render,redirect
from .models import Producto
from .forms import productoForm
from django.http import JsonResponse

# Create your views here.

def agregar_producto(request):
    #revisar como se llego a esta funcion
    if request.method=='POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
    else:
        form= productoForm()
    return render(request,'agregar.html',{'form':form})

def ver_productos(request):
    productos=Producto.objects.all()
    return render(request,'ver.html',{'productos':productos})

#devuelve el Json
def lista_productos(request):
    produtos = Producto.objects.all()
    
    temp= [
        {
            'nombre':p.nombre,
            'precio':p.precio,
            'imagen':p.imagen
        }
        for p in produtos
    ]
    return JsonResponse(temp,safe=False)

def json_view(request):
    return render(request,'json.html')

def registrar_producto(request):
    if request.method=='POST':
        try:
            data= json.loads(request.body)
            nuevo_producto=Producto.objects.create(
                nombre= data['nombre'],
                precio=data['precio'],
                imagen=data['imagen']
            )
            return JsonResponse({
                'mensaje':'registro exitoso',
                'id':nuevo_producto.id
                
            },status=201
            )
        except Exception as e:
            return JsonResponse({
                'error':str(e)
            },status=400)
    return JsonResponse({
        'error': 'Metodo no es POST'
    },status=405)