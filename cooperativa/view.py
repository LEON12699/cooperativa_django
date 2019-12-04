from django.shortcuts import render, render_to_response
from app.login.form import FormularioLogin
from django.template import RequestContext

def homePage(request):
    context = RequestContext(request)
    return render(request,'home_Page.html')