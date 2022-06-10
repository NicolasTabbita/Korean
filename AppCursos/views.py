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

      curso = Capacitacion.objects.get(id=id)

      comentarios = ComentarioForo.objects.filter(curso_id = curso.id)
      if comentarios:
            return render(request, 'AppCursos/foro.html', {'comentarios': comentarios, 'curso': curso})
      else:
            messages.error(request, 'Aun no hay comentarios en este foro.')
            return render(request, 'AppCursos/foro.html', {'comentarios': comentarios, 'curso': curso})


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

