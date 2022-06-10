from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Capacitacion(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = RichTextField()
    fecha_inicio = models.DateTimeField()
    imagen_miniatura = models.ImageField(upload_to='miniaturas_capacitaciones', default = 'miniaturacapacitaciondefault.jpg')
    imagen_portada = models.ImageField(upload_to='portadas_capacitaciones', default = 'portadacapacitaciondefault.jpg')
    link_capacitacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class ComentarioForo(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=80)
    cuerpo = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    curso = models.ForeignKey(Capacitacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class RespuestaForo(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    comentario = models.ForeignKey(ComentarioForo, on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario.titulo
