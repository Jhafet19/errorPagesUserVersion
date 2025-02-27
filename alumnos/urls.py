from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import AlumnoViewSet,agregar_alumnos

router= SimpleRouter()

router.register(r'api',AlumnoViewSet)
urlpatterns=[
    path('',include(router.urls)),
    path('agregar/',agregar_alumnos,name='agregar_alumno')
    
]