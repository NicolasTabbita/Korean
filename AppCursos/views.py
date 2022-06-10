from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ComentarioForoCreationForm, FormacionCreationForm
from .models import Capacitacion, ComentarioForo
from django.contrib import messages

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
                  return foro(request, id)
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
      return foro(request, id_curso)

@login_required
def verComentario(request, id):

      comentario = ComentarioForo.objects.get(id=id)
      respuestas = ComentarioForo.objects.filter(respuestaforo__comentario_id = id)
      return render(request, 'AppCursos/detalleComentario.html', {'comentario': comentario, 'respuestas': respuestas})
