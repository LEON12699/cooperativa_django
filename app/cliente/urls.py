from django.urls import path

from . import views

urlpatterns = [
	path('', views.principal2, name='cliente'),
	path('crear_cliente/', views.crear),
	path('modificar', views.modificar),
	path('cuenta', views.cuenta),
	path('crearCuenta', views.crear_cuenta),
	path('borrar', views.borrar),
	path(r'^deposito/(?P<numero>d+)$', views.depositar, name="deposito"),
	path(r'retiro/(?P<numero>d+)$', views.retirar , name="retiro"),

]