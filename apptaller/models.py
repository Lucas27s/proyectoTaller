from django.db import models
from django.contrib.auth.models import User

# Creacte your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


class Mecanico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    categoria = models.CharField(max_length=50)
    vigente = models.BooleanField(default=True, null=True)
    foto = models.ImageField(default=' ')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre+ " "+self.apellido

class Atencion(models.Model): 
    diagnostico = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    fecha_atencion = models.DateField()
    materiales = models.CharField(max_length=100)
    foto = models.ImageField(default=' ')
    aceptado = models.BooleanField(default=False, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.diagnostico
    
tipos_contacto = [
    [0, "Reclamo"],
    [1, "Sugerencia"],
    [2, "Felicitaciones"]
]

class Contact(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefono = models.IntegerField()
    tipo_contacto = models.IntegerField(choices=tipos_contacto)
    mensaje = models.TextField()
    def __str__ (self):
        return self.nombre + " "+self.email

class Postulacion(models.Model):
    cargo = models.CharField(max_length=100)
    foto = models.ImageField(default=' ')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=50)
    antecedentes_laborales = models.TextField(max_length=300)
    antecedentes_academicos = models.TextField(max_length=300)
    curriculum = models.FileField(default="", null=True)
    def __str__ (self):
        return self.cargo + "-"+self.nombre+ " "+self.apellido



