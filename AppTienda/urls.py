from django.urls import path
from AppTienda import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
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
    path('usuario/contraseña/recuperar/', auth_views.PasswordResetView.as_view(template_name = 'AppTienda/recuperar_contraseña.html'), name = 'password_reset'),
    path('usuario/contraseña/recuperar/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'AppTienda/recuperar_contraseña_done.html'), name = 'password_reset_done'),
    path('usuario/contraseña/recuperar/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'AppTienda/recuperar_contraseña_confirm.html'), name = 'password_reset_confirm'),
    path('usuario/contraseña/recuperar/completado/', auth_views.PasswordResetCompleteView.as_view(template_name = 'AppTienda/recuperar_contraseña_completado.html'), name = 'password_reset_complete'),
    path('about/', views.acerca, name='acerca_de_nosotros'),
]
