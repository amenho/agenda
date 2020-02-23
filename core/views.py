from django.shortcuts import render, redirect
from core.models import Eventos
# Create your views here.

#def index(request):
#    return redirect('/agenda/')

def lista_eventos(request):
   # usuario = request.user
    evento = Eventos.objects.all
    dados = {'eventos':evento}
    return render(request, 'agenda.html',dados)
