from django.urls import path, include
from .views import *
urlpatterns=[
    path('registrar',registrar_categoria,name='registrar'),
    path('api/get',get_categorias_json,name='json_format'),
    path('json/',json_view,name='jsonCategorias'),


]



