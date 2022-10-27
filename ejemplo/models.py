from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    estado_civil = models.CharField(max_length=200,default="")  

    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"


class Usuario(models.Model):

    usuario = models.CharField(max_length=100,unique= True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    password = models.CharField(max_length=100)
    password_dos = models.CharField(max_length=100)

    def __str__(self):
        return f"Usuario:{self.usuario}, Nombre:{self.nombre}, Edad:{self.edad}, ID:{self.id}"

