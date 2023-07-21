from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Vista pagina principal de proyecto.
    """
    return HttpResponse("Prueba pagina principal")