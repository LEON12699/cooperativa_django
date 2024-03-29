from django.db import models

# Create your models here.

class Cliente(models.Model):

	listaGenero = (
		('f', 'Femenino'),
		('m', 'Masculino')
		)

	listaCivil = (
		('soltero', 'Soltero'),
		('casado', 'Casado'),
		('divorciado', 'Divorciado'),
		('viudo', 'Viudo')		
		)

	cliente_id = models.AutoField(primary_key = True)
	cedula = models.CharField(max_length = 10, unique = True, null = False)
	nombre = models.CharField(max_length = 50, null = False)
	apellido = models.CharField(max_length = 50, null = False)	
	genero = models.CharField(max_length = 15, choices = listaGenero, default = 'Femenino', null = False)
	estadoCivil = models.CharField(max_length = 15, choices = listaCivil, default = 'Soltero', null = False)
	correo = models.EmailField(max_length = 50, null = False)
	fechaNacimiento = models.DateField(auto_now = False, auto_now_add = False ,null = False)
	telefono = models.CharField(max_length = 13)
	celular = models.CharField(max_length = 13)
	direccion = models.TextField(max_length = 50, default = "sin direccion")

class Cuenta(models.Model):
	listaTipo = (
		('corriente', 'Corriente'),
		('ahorros', 'Ahorros')
		)

	cuenta_id = models.AutoField(primary_key = True)
	numero = models.CharField("Numero Cuenta:",max_length = 20, unique = True, null = False )
	estado = models.BooleanField(default = True)
	fechaApertura = models.DateField(auto_now_add = True, null = False)
	tipoCuenta = models.CharField(max_length = 30, choices = listaTipo, null = False, default = "ahorros")
	saldo = models.DecimalField(max_digits = 10, decimal_places = 3, null = False)
	cliente = models.ForeignKey('Cliente', on_delete = models.CASCADE,)

	def __str__(self):
		string = str(self.saldo)+";"+str(self.cuenta_id)
		return string

class Transaccion(models.Model):
	listaTipoT = (
		('retiro', 'Retiro'),
		('deposito', 'Deposito'),
		('transferencia', 'Tranferencia')
		)

	transaccion_id = models.AutoField(primary_key = True)
	fechaTransaccion = models.DateTimeField(auto_now_add = True, null = False)
	tipoTransaccion = models.CharField(max_length = 30, choices = listaTipoT, null = False)
	valor = models.DecimalField(max_digits = 10, decimal_places = 3, null = False)
	descripcion = models.TextField(null = False)
	responsable = models.CharField(max_length = 160, null = False)
	cuenta = models.ForeignKey(
		'Cuenta',
		on_delete = models.CASCADE,
		)			