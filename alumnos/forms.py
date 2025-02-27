from django import forms
from .models import Alumnos

class  alumnoForm(forms.ModelForm):
    class Meta:
        model=Alumnos
        fields=['nombre','Apellido','Edad','Matricula','Correo']
        widgets={
            'nombre':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese un nombre para el alumno'
                }
            ),
            'Apellido':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese un apellido para el alumno'
                }
            ),
            'Edad':forms.NumberInput(
                attrs={
                         'class':'form-control',
                    'placeholder':'Ingrese un apellido para el alumno'
                
                    }),
            'Matricula':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese una matricula  para el alumno'
                }
            ),
            'Correo':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese un correo para el alumno'
                }
            )
        }