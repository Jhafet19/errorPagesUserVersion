# Create your views here.

from django.shortcuts import render
from .models import Alumnos
from .serializers import AlumnosSerializar
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .forms import alumnoForm


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    serializer_class = AlumnosSerializar
    renderer_classes = [JSONRenderer]


def agregar_alumnos(request):
    form = alumnoForm
    return render(request, "rodriguez_jhafet.html", {"form": form})
