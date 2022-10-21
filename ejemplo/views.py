from urllib import request
from django import views
from django.http import HttpResponse
from django.shortcuts import render
from ejemplo.models import Familiar, Usuario
from ejemplo.forms import Buscar
from django.views import View
from ejemplo.forms import abmCargar

def index(request):
    return render(request, "ejemplo/saludar.html")
    
def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})
 
class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})

def abm(request):
    return render(request, "ejemplo/abm.html")

class ABMCargar(View):

    form_class = abmCargar
    template_name = 'ejemplo/abm_cargar.html'
    initial = {"usuario":"",
                "nombre":"",
                "edad":"",
                "password":"",
                "password_dos":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            
            un_usuario = Usuario(usuario= form.cleaned_data.get("usuario"),
                    nombre = form.cleaned_data.get("nombre"),
                    edad = form.cleaned_data.get("edad"),
                    password = form.cleaned_data.get("password"),
                    password_dos = form.cleaned_data.get("password_dos"))
            un_usuario.save()
                    
            form = self.form_class(initial=self.initial)
            return render(request,"ejemplo/abm_borrar.html",{"usuario":un_usuario.usuario,"accion":"Guardado"})

        return render(request, self.template_name, {"form": form})
        

class BuscarABM(View):

    form_class = Buscar
    template_name = 'ejemplo/abm_buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            usuario = Usuario.objects.filter(usuario__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'usuario':usuario})

        return render(request, self.template_name, {"form": form})

def borrar (request,usuario):
    un_usuario = Usuario.objects.filter(usuario__icontains=usuario).all()
    id = usuario
    un_usuario.delete()
    return render(request,"ejemplo/abm_borrar.html",{"usuario":id,"accion":"Borrado"})

def modificar(request, usuario):

    un_usuario = Usuario.objects.get(usuario=usuario)

    if request.method == 'POST':

        miFormulario = abmCargar(request.POST)

        if miFormulario.is_valid: 

            informacion = miFormulario.cleaned_data

            un_usuario.usuario = informacion['usuario']
            un_usuario.nombre = informacion['nombre']
            un_usuario.edad = informacion['edad']
            un_usuario.password = informacion['password']
            un_usuario.password_dos = informacion['password_dos']

            un_usuario.save()

            return render(request, "ejemplo/abm_borrar.html",{"usuario":un_usuario.usuario,"accion":"Modificado"})
    else:
        
        miFormulario = abmCargar(initial={'usuario': un_usuario.usuario, 'nombre': un_usuario.nombre,
                                                   'edad': un_usuario.edad, 'password': un_usuario.password,
                                                   'password_dos': un_usuario.password_dos})

    return render(request, "ejemplo/abm_modificar.html", {"miFormulario": miFormulario, "usuario": un_usuario})
