from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ComentarioForoCreationForm, FormacionCreationForm, RespuestaForoCreationForm
from .models import Capacitacion, ComentarioForo, RespuestaForo
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
import os
# Capacitaciones
def capacitaciones(request):
    
      cursos_lista = Capacitacion.objects.all()

      return render(request, 'AppCursos/formacion.html', {'cursos_lista': cursos_lista})

def capacitacionDetalle(request,id):

      curso = Capacitacion.objects.get(id=id)

      return render(request, 'AppCursos/formacionDetalle.html', {'curso': curso})

@staff_member_required
def crearCapacitacion(request):

      if request.method == 'POST':

            form = FormacionCreationForm(request.POST, request.FILES)

            if form.is_valid():
                  info = form.cleaned_data
                  nuevaCapacitacion = Capacitacion(nombre=info['nombre'],precio=info['precio'],descripcion=info['descripcion'],fecha_inicio=info['fecha_inicio'],
                  imagen_miniatura=info['imagen_miniatura'],imagen_portada=info['imagen_portada'],link_capacitacion=info['link_capacitacion'])

                  nuevaCapacitacion.save()

                  messages.success(request, 'capacitacion creada con exito!')
                  return redirect('cursos:capacitaciones')
      else:
            form = FormacionCreationForm()

      return render(request, 'AppCursos/crearFormacion.html', {'form': form})

@staff_member_required
def eliminarCapacitacion(request,id):
      formacion = Capacitacion.objects.get(id=id)
      formacion.delete()

      messages.success(request, 'Formacion eliminada.')
      return redirect('cursos:capacitaciones')

@staff_member_required
def editarCapacitacion(request,id):
      capacitacion = Capacitacion.objects.get(id=id)
      
      if request.method == 'POST':

            form = FormacionCreationForm(request.POST, request.FILES, instance=capacitacion)

            if form.is_valid():

                  capacitacion.save()

                  messages.success(request, 'capacitacion editada con exito!')
                  return redirect('cursos:capacitaciones')
      else:
            form = FormacionCreationForm(instance=capacitacion)

      return render(request, 'AppCursos/editarFormacion.html', {'form': form})

# Foro

@login_required
def foro(request, id):

      usuario = request.user
      cursos_usuario = Capacitacion.objects.filter(operaciones__usuario_id=usuario.id)
      curso = Capacitacion.objects.get(id=id)
      if curso in cursos_usuario:
            comentarios = ComentarioForo.objects.filter(curso_id = curso.id)
            if not comentarios:
                  messages.error(request, 'Aun no hay comentarios en este foro.')
            return render(request, 'AppCursos/foro.html', {'comentarios': comentarios, 'curso': curso})
      else:
            messages.error(request, 'Solo puedes acceder a los foros de las formaciones que poseas.')
            return redirect('mis_capacitaciones')


@login_required
def crearComentario(request, id):

      curso = Capacitacion.objects.get(id=id)
      
      if request.method == 'POST':
            
            form = ComentarioForoCreationForm(request.POST)

            if form.is_valid():
                  info = form.cleaned_data
                  mi_comentario = ComentarioForo(usuario = request.user, titulo = info['titulo'], cuerpo = info['cuerpo'], curso = curso)
                  mi_comentario.save()

                  messages.success(request, 'Comentario publicado con exito.')
                  return redirect('cursos:foro', id=id)
      else:
            form = ComentarioForoCreationForm()
      
      return render(request, 'AppCursos/crearComentario.html', {'form': form})

@login_required
def eliminarComentario(request, id):

      comentario = ComentarioForo.objects.get(id=id)
      curso = Capacitacion.objects.filter(comentarioforo__id = comentario.id)
      id_curso = curso[0].id
      if comentario.usuario == request.user:            
            comentario.delete()
            messages.success(request, 'Comentario eliminado con exito')
      else:
            messages.error(request, 'Solo puedes eliminar tus comentarios')
      return redirect('cursos:foro', id=id_curso)

@login_required
def crearRespuesta(request, id):
# muestra el detalle del comentario junto con el formulario para crear una nueva respuesta
      comentario = ComentarioForo.objects.get(id=id)
      respuestas = RespuestaForo.objects.filter(comentario_id = id)
      usuario = comentario.usuario
      if request.method == 'POST':

            form = RespuestaForoCreationForm(request.POST)

            if form.is_valid():

                  info = form.cleaned_data
                  mi_respuesta = RespuestaForo(usuario = request.user, cuerpo = info['cuerpo'], comentario = comentario)
                  mi_respuesta.save()

                  messages.success(request, 'Respuesta publicada con exito')                 

                  if usuario != request.user:
                        url = reverse('cursos:nueva_respuesta', kwargs={'id':comentario.id})
                        send_mail(
                              'Recibiste una nueva respuesta en el foro!',
                              f'Hola {usuario.username}, recibiste una nueva respuesta de {request.user.username} a tu publicacion en el foro. \n Podes ver el hilo completo desde http://{request.get_host()}{url}',
                              os.environ.get('EMAIL_USER'),
                              [usuario.email],
                              fail_silently = False,
                        )
                  return render(request, 'AppCursos/crearRespuesta.html', {'comentario': comentario, 'respuestas': respuestas, 'form': RespuestaForoCreationForm()})
      else:
            form = RespuestaForoCreationForm()

      return render(request, 'AppCursos/crearRespuesta.html', {'comentario': comentario, 'respuestas': respuestas, 'form': form})

            
