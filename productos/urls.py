from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductoViewSet, agregar_producto

router = SimpleRouter()

router.register(r"api", ProductoViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("agregar/", agregar_producto, name="agregar_productos"),
]
