from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def index(request):
    """
    Vista pagina principal de proyecto.
    """
    return render(request, "contacts/index.html")


def contact_list(request):
    """
    Vista lista de contactos guardados.
    """
    return render(request, "contacts/list.html")


def exit(request):
    """
    Funcion de logout del proyecto.
    """
    logout(request)
    return redirect("index")