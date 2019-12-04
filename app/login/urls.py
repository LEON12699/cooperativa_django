from django.urls import path

from . import views

urlpatterns = [
    path('', views.ingresar, name="autenticar"),
    path('logout', views.cerrar, name="cerrar_sesion"),
]
