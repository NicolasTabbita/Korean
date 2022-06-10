from dataclasses import field, fields
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Capacitacion, ComentarioForo, RespuestaForo

class FormacionCreationForm(forms.ModelForm):
    nombre = forms.CharField()
    precio = forms.IntegerField()
    descripcion = forms.CharField(widget=CKEditorWidget())
    fecha_inicio = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    imagen_miniatura = forms.ImageField()
    imagen_portada = forms.ImageField()
    link_capacitacion = forms.CharField()

    class Meta:
        model = Capacitacion
        fields = '__all__'

class ComentarioForoCreationForm(forms.ModelForm):
    titulo = forms.CharField()
    cuerpo = forms.CharField()

    class Meta:
        model = ComentarioForo
        fields = ['titulo', 'cuerpo']

class RespuestaForoCreationForm(forms.ModelForm):
    cuerpo = forms.CharField()

    class Meta:
        model = RespuestaForo
        fields = ['cuerpo']