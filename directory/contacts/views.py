from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Contact
from .forms import CreateNewContact


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
    contacts = Contact.objects.all()
    return render(request, "contacts/list.html", {"contacts":contacts})


def create_contact(request):
    """
    Vista de creación de contactos
    """
    if request.method == "GET":
        return render(request, "contacts/create_contact.html", {"form": CreateNewContact()})
    else:
        Contact.objects.create(name=request.POST["name"], number=request.POST["number"])
        return redirect("/list")


def exit(request):
    """
    Funcion de logout del proyecto.
    """
    logout(request)
    return redirect("index")