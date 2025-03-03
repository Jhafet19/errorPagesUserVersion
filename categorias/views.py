from django.shortcuts import render, redirect
from .forms import categoriaForm
from .models import Categoria
from django.http import JsonResponse


# Create your views here.
def registrar_categoria(request):
    if request.method == "POST":
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jsonCategorias")
    form = categoriaForm()
    return render(request, "registrarCategoria.html", {"form": form})


def get_categorias_json(request):
    categorias = Categoria.objects.all()

    json = [
        {
            "nombre": c.nombre,
            "imagen": c.imagen,
        }
        for c in categorias
    ]
    return JsonResponse(json, safe=False)


def json_view(request):
    print("Pasando por json_view")
    return render(request, "jsonCategorias.html")
