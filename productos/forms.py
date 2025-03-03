from .models import Producto
from django import forms


# Podemos crar un formulario para cada modelo que exista
class productoForm(forms.ModelForm):
    class Meta:
        # Definir de que
        model = Producto
        fields = ["nombre", "precio", "imagen"]
        # Definir como se deben de ver o que atributos tinen los campos
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre del producto",
                }
            ),
            "precio": forms.NumberInput(
                attrs={"class": "form-control", "palceholder": "Precio"}
            ),
            "imagen": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "palceholder": "url de la imagen del producto",
                }
            ),
        }

        labels = {
            "nombre": "nombre del producto",
            "precio": "precio en moneda nacional",
            "imagen": "URl de la imagen",
        }

        # Mensajes de error personalisados
        error_messeges = {
            "nombre": {
                "required": "El nombre es obligatorio",
            },
            "precio": {
                "required": "El precio no puede ser vacio",
                "invalid": "Ingrese un numero valido",
            },
        }
