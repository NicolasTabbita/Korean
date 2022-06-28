from django.urls import path
from .views import agregarCarrusel, agregarProductoEstrella, crearPublicacion, editarCarrusel, editarProdEstrella, editarPublicacion, eliminarCarrusel, eliminarProdEstrella, eliminarPublicacion, imagenesCarrusel, publicacionDetalle, publicaciones, verProdEstrella, inicio

app_name = 'blog'

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('publicaciones/', publicaciones, name='lista_publicaciones'),
    path('publicaciones/detalle/<id>', publicacionDetalle, name='publicacion_detalle'),
    path('publicaciones/crear/', crearPublicacion, name='crear_publicacion'),
    path('publicaciones/eliminar/<id>', eliminarPublicacion, name='eliminar_publicacion'),
    path('publicaciones/editar/<id>', editarPublicacion, name='editar_publicacion'),
    path('carrusel/crear/', agregarCarrusel, name='crear_carrusel'),
    path('carrusel/imagenes/', imagenesCarrusel, name='imagenes_carrusel'),
    path('carrusel/editar/<id>', editarCarrusel, name='editar_carrusel'),
    path('carrusel/eliminar/<id>', eliminarCarrusel, name='eliminar_carrusel'),
    path('producto/estrella/crear/', agregarProductoEstrella, name='agregar_prod_estrella'),
    path('producto/estrella/eliminar/<id>', eliminarProdEstrella, name='eliminar_prod_estrella'),
    path('producto/estrella/editar/<id>', editarProdEstrella, name='editar_prod_estrella'),
    path('producto/estrella/', verProdEstrella, name='ver_prod_estrella'),
]
