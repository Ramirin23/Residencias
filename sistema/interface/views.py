from django.shortcuts import render
from django.http import HttpResponse
from .models import Narrativa

# Create your views here.


def inicio(request):
    return HttpResponse("<h1>Bienvenido</h1>")


def view(request):
    return render(request, 'pages/view.html')


def lista_narrativas(request):
    print("Se está llamando a lista_narrativas")
    narrativas = Narrativa.objects.all()
    return render(request, 'pages/view.html', {'narrativas': narrativas})
