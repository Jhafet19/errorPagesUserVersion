from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
import re
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Correo electrónico",
                "required": True,
                "pattern": "^[0-9]{5}[a-zA-Z]{2}[0-9]{3}@utez\.edu\.mx$",
                "title": "Debe contar con un correo institucional",
                "id": "correoInput",
            }
        ),
    )
    name = forms.CharField(
        label="Nombre completo",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese su nombre",
                "required": True,
                "minlength": "3",
                "maxlength": "100",
                "pattern": "^[a-zA-Z ]+$",
                "title": "Solo se permiten letras y espacios",
                "id": "nombreInput",
            }
        ),
    )
    surname = forms.CharField(
        label="Apellido",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese su apellido",
                "required": True,
                "minlength": "3",
                "maxlength": "100",
                "pattern": "^[a-zA-Z ]+$",
                "title": "Solo se permiten letras y espacios",
                "id": "apellidoInput",
            }
        ),
    )
    control_number = forms.CharField(
        label="Matrícula",
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Número de control",
                "required": True,
                "pattern": "^[0-9]{5}[a-zA-Z]{2}[0-9]{3}$",
                "title": "Solo se permiten matrículas de la UTEZ",
                "id": "matriculaInput",
            }
        ),
    )
    age = forms.IntegerField(
        label="Edad",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Edad",
                "required": True,
                "min": "18",
                "max": "100",
                "title": "Debe ser un número entre 18 y 100",
                "id": "edadInput",
            }
        ),
    )
    tel = forms.CharField(
        label="Teléfono",
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Número telefónico",
                "required": True,
                "pattern": "^[0-9]{10}$",
                "title": "Debe ser un número de teléfono de 10 dígitos",
                "id": "telefonoInput",
            }
        ),
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Contraseña",
                "required": True,
                "title": "Debe tener al menos 8 caracteres, incluir un número y un símbolo (!, #, $, %, & o ?).",
                "id": "id_password1",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirmar contraseña",
                "required": True,
                "title": "Debe coincidir con la contraseña anterior.",
                "id": "id_password2",
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "name",
            "surname",
            "control_number",
            "age",
            "tel",
            "password1",
            "password2",
        ]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not re.match(r"^[0-9]{5}[a-zA-Z]{2}[0-9]{3}@utez\.edu\.mx$", email):
            raise ValidationError(
                "El correo electrónico debe pertenecer al dominio @utez.edu.mx"
            )
        return email

    def clean_name(self):
        print("en clean name")
        name = self.cleaned_data.get("name")
        print(f"name: {name}")
        if not re.match(r"^[a-zA-Z ]{1,100}$", name):
            raise ValidationError(
                "El nombre solo debe contener letras y espacios, y no debe superar los 100 caracteres."
            )
        return name

    def clean_surname(self):
        surname = self.cleaned_data.get("surname")
        print(f"surname: {surname}")
        if not re.match(r"^[a-zA-Z ]{1,100}$", surname):
            raise ValidationError(
                "El apellido solo debe contener letras y espacios, y no debe superar los 100 caracteres."
            )
        return surname

    def clean_control_number(self):
        control_number = self.cleaned_data.get("control_number")
        if not re.match(r"^[0-9]{5}[a-zA-Z]{2}[0-9]{3}$", control_number):
            raise ValidationError("La matrícula debe pertenecer a la UTEZ")
        return control_number

    def clean_tel(self):
        tel = self.cleaned_data.get("tel")
        if not re.match(r"^[0-9]{10}$", tel):
            raise ValidationError("El numero telefonico debe tener 10 caracteres")
        return tel

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if not re.match(r"^(?=.*\d)(?=.*[!#$%&?]).{8,}$", password1):
            raise ValidationError(
                "La contraseña debe tener al menos 8 caracteres, incluir un número y un símbolo (!, #, $, %, & o ?)."
            )
        return password1

    def clean(self):
        cleaned_data = super().clean()
        print("provando contraseñas")
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        print("Despues del scouting")

        if password1 and password2 and password1 != password2:
            print("en el IF")
            raise ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    """password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': True,
            'placeholder': 'Contraseña',
            'minlength': '8',
            'pattern': '^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$',
            'title': 'Debe contener al menos 8 caracteres, una mayúscula, un número y un carácter especial (!#$%&?)',
            'id': 'password1'
        }) ) """


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Correo electrónico",
                "required": True,
                "pattern": "^[0-9]{5}[a-zA-Z]{2}[0-9]{3}@utez\.edu\.mx$",
                "title": "Debe ser un correo institucional con el formato: 12345tn678@utez.edu.mx",
            }
        ),
    )


password = forms.CharField(
    widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Contraseña",
            "required": True,
        }
    )
)
