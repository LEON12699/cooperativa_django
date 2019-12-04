from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .Forms import FormularioCliente
from .Forms import FormularioCuenta, FormularioModificar,FormularioTransaccion
from app.cliente.models import Cliente
from app.cliente.models import Cuenta
from app.cliente.models import Transaccion
from django.contrib import messages
from . import services
# Create your views here.


def generarnumero():
    numero = Cuenta.objects.count()
    valor = "01-0432"+str(numero)
    while(Cuenta.objects.filter(numero=valor).exists()):
        numero= numero+1
        valor="01-0432"+str(numero)    
    
    
    return valor
# alogin required
@login_required
def crear_cuenta(request):
    dni = request.GET['cedula']
    try:
        cliente = Cliente.objects.get(cedula=dni)
    except Cliente.DoesNotExist:
        messages.error(request , 'error en busqueda de cliente')
        return redirect(principal)        #cliente=None

    formularioCuenta = FormularioCuenta(request.POST, initial={'numero': generarnumero()})
    usuario = request.user # peticion procesada por el framework si no existe lo pone en null
    if usuario.groups.filter(name='cajero').exists() :#usuario.groups.filter(name="administrativo").exists():    
        if request.method == 'POST':
            if formularioCuenta.is_valid():
                datosCuenta = formularioCuenta.cleaned_data
                
                cuentad = Cuenta()
                
                cuentad.numero = datosCuenta.get('numero')
                cuentad.estado = True
                cuentad.fechaApertura = datosCuenta.get('fechaApertura')
                cuentad.tipoCuenta = datosCuenta.get('tipoCuenta')
                cuentad.saldo = datosCuenta.get('saldo')
                cuentad.cliente = cliente
                cuentad.save()
                return redirect('/cliente/cuenta?cedula='+dni)
    else: 
        return render(request, 'error.html', context={'mensaje': 'NO TIENES PERMISOS'})
    
    context={
        'dni':dni,
        'f':formularioCuenta
    }   
    return render(request,'cuenta/crear.html',context)

@login_required
def borrar(request):
    dni = request.GET['cedula']
    cliente = Cliente.objects.get(cedula=dni)
    cliente.delete()
    return redirect(principal)
    
@login_required
def cuenta(request):
    dni = request.GET['cedula']
    try:
        cliente = Cliente.objects.get(cedula=dni)
    except Cliente.DoesNotExist:
        messages.error(request , 'cliente no existe')
        return redirect(principal)
    LCuenta = Cuenta.objects.filter(cliente_id=cliente.cliente_id)
    context = {
        'lista':LCuenta,
        'dni':dni
        }
    return render(request, 'cuenta/crear_cuenta.html', context)
    

def principal(request):
    lista = Cliente.objects.all().order_by('apellido')
    context = {
        'lista': lista,
    }
    return render(request, 'cliente/principal_cliente.html', context)

def principal2(request):
    lista = services.get_cliente()
    context = {
        'lista': lista['clientes'],
    }
    
    return render(request, 'cliente/principal_cliente.html', context)


@login_required
def crear(request):
    formularioCuenta = FormularioCuenta(request.POST, initial={'numero':generarnumero()})
    formulario = FormularioCliente(request.POST)
    usuario = request.user # peticion procesada por el framework si no existe lo pone en null
    
    print(usuario.get_all_permissions())
    if usuario.has_perm('cliente.add_cliente') :#usuario.groups.filter(name="administrativo").exists():
        
        if request.method == 'POST':
            if formulario.is_valid() and formularioCuenta.is_valid():
                # obteniendo todos los datos del formulario del cliente
                datos = formulario.cleaned_data
                cliente = Cliente()
                cliente.cedula = datos.get('cedula')
                cliente.nombre = datos.get('nombre')
                cliente.apellido = datos.get('apellido')
                cliente.genero = datos.get('genero')
                cliente.fechaNacimiento = datos.get('fechaNacimiento')
                cliente.telefono = datos.get('telefono')
                cliente.celular = datos.get('celular')
                cliente.direccion = datos.get('direccion')
                cliente.correo = datos.get('correo')
                cliente.estadoCivil = datos.get('estadoCivil')
                cliente.save()

                # obteniendo todos los datos del formulario cuenta
                datosCuenta = formularioCuenta.cleaned_data
                cuenta = Cuenta()
                cuenta.numero = datosCuenta.get('numero')
                cuenta.estado = True
                cuenta.fechaApertura = datosCuenta.get('fechaApertura')
                cuenta.tipoCuenta = datosCuenta.get('tipoCuenta')
                cuenta.saldo = datosCuenta.get('saldo')
                cuenta.cliente = cliente
                cuenta.save()
                messages.success(request , 'se creo el cliente exitosamente')
# usuario.has_perm('modelo_add_cliente') para permisos
                return redirect(principal)
    else: 
        return render(request, 'error.html', context={'mensaje': 'NO TIENES PERMISOS'})
    context = { 
        'f': formulario,
        'fc': formularioCuenta
    }

    return render(request, 'cliente/crear_cliente.html', context)

@login_required
def modificar(request):
    dni = request.GET['cedula']
    try:
        cliente = Cliente.objects.get(cedula=dni)
    except Cliente.DoesNotExist:
        messages.error(request , 'error en busqueda de cliente')
        return redirect(principal)
    
    if request.method == 'POST':
            formulario = FormularioModificar(request.POST ) # ya veiene cargados los elemertos por el get primeor ejecutado
            if formulario.is_valid():
                datos=formulario.cleaned_data
                
                cliente.nombre = datos.get('nombre')
                cliente.apellido = datos.get('apellido')
                cliente.genero = datos.get('genero')
                cliente.fechaNacimiento = datos.get('fechaNacimiento')
                cliente.telefono = datos.get('telefono')
                cliente.celular = datos.get('celular')
                cliente.direccion = datos.get('direccion')
                cliente.correo = datos.get('correo')
                cliente.estadoCivil = datos.get('estadoCivil')
                cliente.save()
                return redirect(principal)
    else:
        formulario = FormularioModificar(instance=cliente)
    context = {
        'dni': dni,
        'cliente': cliente,
        'f': formulario
        }
        
    
    # examinar linea xde codigo formulario = FormularioCliente(request.POST)
	
    return render(request, 'cliente/modificar_cli.html', context)

@login_required
def depositar(request,numero):
    try:
        cuenta = Cuenta.objects.get(numero=numero)
    except Cuenta.DoesNotExist:
        messages.error(request , 'no se pudo encontrar la cuenta')
        return redirect(principal)
    cliente = Cliente.objects.get(cliente_id = cuenta.cliente_id)
    formulario = FormularioTransaccion(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            
            datos = formulario.cleaned_data
            cuenta.saldo = cuenta.saldo + datos.get('valor')
            cuenta.save()
            transaccion = Transaccion()
            transaccion.tipo = 'Deposito'
            transaccion.valor =  datos.get('valor')
            transaccion.descripcion = datos.get('descripcion')
            transaccion.responsable = 'cualquiersierasdasda'
            
            transaccion.cuenta = cuenta
            transaccion.save()
            messages.success(request, 'transaccion exitosa')
            #messages.add_message(request, messages.INFO, 'Hello world.')
            return redirect("/cliente/cuenta?cedula="+cliente.cedula) # locals() se llevan todas las variable
            
    context={
        'formulario': formulario,
        'cuenta':cuenta,
        'cliente':cliente
    }    
    return render(request, 'transaccion/depositar.html', context)
    

@login_required
def retirar(request,numero):
    try:
        cuenta = Cuenta.objects.get(numero=numero)
    except Cuenta.DoesNotExist:
        messages.error(request , 'no se pudo encontrar la cuenta')
        return redirect(principal)
    cliente = Cliente.objects.get(cliente_id = cuenta.cliente_id)
    formulario = FormularioTransaccion(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            
            datos = formulario.cleaned_data
            cuenta.saldo = cuenta.saldo - datos.get('valor')
            cuenta.save()
            transaccion = Transaccion()
            transaccion.tipo = 'Retiro'
            transaccion.valor =  datos.get('valor')
            transaccion.descripcion = datos.get('descripcion')
            transaccion.responsable = 'cualquiersierasdasda'
            
            transaccion.cuenta = cuenta
            transaccion.save()
            messages.success(request, 'retiro exitoso')
            return redirect("/cliente/cuenta?cedula="+cliente.cedula)
            
    context={
        'formulario': formulario,
        'cuenta':cuenta,
        'cliente':cliente
    }    
    return render(request, 'transaccion/retirar.html', context)
