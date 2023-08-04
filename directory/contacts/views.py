from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


def signup(request):
    """
    Vista creación de usuarios
    """
    if request.method == "GET":
        return render(request, "registration/signup.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user_creation = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user_creation.save()
                redirect("contacts/index.html")
            except:
               return render(request, "registration/signup.html", {"form": UserCreationForm,
                                                            "error": "Usuario ya existe"})
        return render(request, "registration/signup.html", {"form": UserCreationForm,
                                                            "error": "Las contraseñas no coinciden."})    


def exit(request):
    """
    Funcion de logout del proyecto.
    """
    logout(request)
    return redirect("index")