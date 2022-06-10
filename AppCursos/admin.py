from django.contrib import admin
from .models import Capacitacion, ComentarioForo, RespuestaForo

# Register your models here.

admin.site.register(ComentarioForo)
admin.site.register(RespuestaForo)