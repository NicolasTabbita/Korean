from django.urls import path
from AppCursos import views

app_name = 'cursos'

urlpatterns = [
    path('disponibles/', views.capacitaciones, name="capacitaciones"),
    path('disponibles/detalle/<id>', views.capacitacionDetalle, name="capacitacion_detalle"),
    path('disponibles/crear', views.crearCapacitacion, name="nueva_capacitacion"),
    path('disponibles/eliminar/<id>', views.eliminarCapacitacion, name="eliminar_capacitacion"),
    path('disponibles/editar/<id>', views.editarCapacitacion, name="editar_capacitacion"),
    path('foro/comentario/nuevo/<id>', views.crearComentario, name="nuevo_comentario"),
    path('foro/comentario/eliminar/<id>', views.eliminarComentario, name="eliminar_comentario"),
    path('foro/comentario/respuesta/<id>', views.crearRespuesta, name="nueva_respuesta"),
    path('foro/<id>', views.foro, name="foro"),
]