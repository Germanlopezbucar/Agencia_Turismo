from django import forms
from django.forms import ValidationError
from ejemplo.models import Usuario
 
class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100, empty_value=" ")

class abmCargar(forms.Form):

    usuario = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    edad = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    password_dos = forms.CharField(max_length=100)


    def clean_usuario(self):
        usuario = self.cleaned_data.get("usuario")
        if usuario[0].isnumeric() or len(usuario) < 3:
                raise ValidationError ("El usuario tiene que ser mayor a 3 caracteres y no puede comenazar con un numero")
        user = Usuario.objects.filter(usuario = usuario).exists()
        if user: 
                raise ValidationError ("El usuario ya existe")

        return usuario

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if len(nombre) < 3:
            raise ValidationError ("El nombre tiene que ser mayor a 3 caracteres")
        return nombre  

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 3 and ('#' not in password or '%' not in password):
            raise ValidationError("EL password tiene que ser mayor a 3 caracteres y tiene que tener un # o %")
        return password

    def clean_password_dos(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password_dos")
        if password != password2:
            raise ValidationError ("La contraseñas ingresadas no coinciden")
        return password2

