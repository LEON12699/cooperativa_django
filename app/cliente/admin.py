from django.contrib import admin

# Register your models here.

from.models import Cliente
from.models import Cuenta
from.models import Transaccion

class AdminCliente(admin.ModelAdmin):
	list_display = ["cedula", "apellido", "nombre", "genero"]
	list_editable = ["apellido", "nombre"]
	list_filter = ["genero", "estadoCivil"]
	search_fields = ["cedula", "apellido", "nombre"]

	class Meta:
		model = Cliente

admin.site.register(Cliente, AdminCliente)

class AdminCuenta(admin.ModelAdmin):
	list_display = ["numero", "estado", "tipoCuenta", "saldo", "cliente"]
	list_editable = ["estado"]
	list_filter = ["estado"]
	search_fields = ["numero", "tipoCuenta", "cliente"]

	class Meta:
		model = Cuenta

admin.site.register(Cuenta, AdminCuenta)

class AdminTransaccion(admin.ModelAdmin):
	list_display = ["fechaTransaccion", "tipoTransaccion", "valor", "cuenta"]	
	list_filter = ["tipoTransaccion"]
	search_fields = ["cuenta", "fechaTransaccion"]

	class Meta:
		model = Transaccion

admin.site.register(Transaccion, AdminTransaccion)