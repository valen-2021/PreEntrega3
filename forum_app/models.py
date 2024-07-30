from django.db import models


class Personal(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    passw = models.CharField(max_length=40)
    edad = models.IntegerField()

class Negocios(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    passw = models.CharField(max_length=40)

class Admins(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

    

# Create your models here.
