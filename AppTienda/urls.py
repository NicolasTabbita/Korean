from django.urls import path
from AppTienda import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('producto/nuevo/<id>', views.agregarProducto, name="agregar_producto"),
    path('producto/eliminar/<id>', views.eliminarProducto, name="eliminar_producto"),
    path('carrito/', views.verCarrito, name="carrito"),
    path('comprar/', views.comprar, name="comprar"),
    path('usuario/capacitaciones/', views.misCursos, name="mis_capacitaciones"),
    path('usuario/registrarse/', views.crearUsuario, name="registro_usuario"),
    path('usuario/login/', views.loginRequest, name="login"),
    path('usuario/perfil/', views.editarUsuario, name="editar_usuario"),
    path('usuario/logout/', LogoutView.as_view(template_name = 'AppTienda/logout.html'), name = 'logout'),
    path('about/', views.acerca, name='acerca_de_nosotros'),
]
