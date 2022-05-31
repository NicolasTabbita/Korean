from django.db import models
from django.contrib.auth.models import User
from AppCursos.models import Capacitacion

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Capacitacion)
    total = models.IntegerField()

class Operaciones(models.Model):

    fecha_compra = models.DateField(auto_now=True, auto_now_add=False)
    producto = models.ManyToManyField(Capacitacion)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    