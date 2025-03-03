from django import forms
from .models import Categoria


class categoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre", "imagen"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese un nombre para la categoria",
                }
            ),
            "imagen": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Urlpara la imagen",
                }
            ),
        }
        labels = {"nombre": "nombre de la categoria", "imagen": "URl de la imagen"}
