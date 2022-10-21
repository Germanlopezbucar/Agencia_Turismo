from email.policy import default
from django import forms

from ejemplo.models import Usuario
 
class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100, empty_value=" ")

class abmCargar(forms.Form):
    usuario = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    edad = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    password_dos = forms.CharField(max_length=100)

