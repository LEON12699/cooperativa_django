from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .form import FormularioLogin
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def  ingresar(request):
    if request.method =='POST':
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            
            clave = request.POST['password']
            
            user = authenticate(username = usuario,password = clave)
            #print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('cliente'))
                else: 
                    print('usuario desactivado')
            else:
                print ('Usuario o contraseña incorrecta')
    else:
        formulario = FormularioLogin()        
    context = {
        'form':formulario,
    }
    return render(request, "login/login.html",context)

def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')