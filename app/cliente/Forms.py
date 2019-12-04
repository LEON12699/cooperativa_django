from django import forms;
from app.cliente.models import Cliente;
from app.cliente.models import Cuenta;
from app.cliente.models import Transaccion;


class FormularioCliente(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ["cedula", "nombre", "apellido", "genero", "fechaNacimiento", "estadoCivil", "telefono", "celular", "direccion", "correo"]

class FormularioModificar(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "genero", "fechaNacimiento", "estadoCivil", "telefono", "celular", "direccion", "correo"]
   # def __init__(self, *args, **kwargs):
    #    super(FormularioModificar, self).__init__(*args, **kwargs)
     #   self.fields['cedula'].disabled = True

class FormularioCuenta(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ["numero","tipoCuenta", "saldo"]
    def __init__(self, *args, **kwargs): 
        super(FormularioCuenta, self).__init__(*args, **kwargs)
        self.fields['numero'].disabled = True
    
    

class FormularioTransaccion(forms.ModelForm):
	class Meta: 
		model = Transaccion
		fields = ["valor", "descripcion"]