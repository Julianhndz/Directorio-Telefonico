from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Contact
from .forms import CreateNewContact


def index(request):
    """
    Vista pagina principal de proyecto.
    """
    return render(request, "contacts/index.html")


@login_required
def contact_list(request):
    """
    Vista lista de contactos guardados.
    """
    # Verificar si el usuario esta autenticado
    if request.user.is_authenticated:
        # Obtener los contactos del usuario autenticado
        contacts = Contact.objects.filter(contactuser__user=request.user)
    else:
        # Si el usuario no esta autenticado, no mostrar contactos
        contacts = []
    return render(request, "contacts/list.html", {"contacts":contacts})


@login_required
def create_contact(request):
    """
    Vista de creación de contactos
    """
    if request.method == "GET":
        # Muestra formulario para creación de contacto
        return render(request, "contacts/create_contact.html", {"form": CreateNewContact()})
    else:
        # Creación de contacto asociandolo al usuario que este autenticado
        new_contact = Contact.objects.create(name=request.POST["name"], number=request.POST["number"])
        # Asociación al usuario mediante la tabla intermedia ContactUser
        new_contact.users.add(request.user)
        return redirect("/list")


def signup(request):
    """
    Vista creación de usuarios
    """
    if request.method == "GET":
        # Muestra formulario para creación de nuevo usuario
        return render(request, "registration/signup.html", {"form": UserCreationForm})
    else:
        # Validación de contraseñas. Si la comparación da True, pasa al Try/Except, para validación y manejo de errores 
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # Intenta creación de usuario, si no hay error se guarda en modelo User y se crea un usuario para uso.
                user_creation = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user_creation.save()
                login(request, user_creation)
                return redirect("index")
            except IntegrityError:
               # Se maneja el error de que el nombre del usuario que se quiere crear sea igual a uno ya existente. Django hace la comparación de manera automatica, acá solamente mostramos un mensaje de error en pantalla.
               return render(request, "registration/signup.html", {"form": UserCreationForm,
                                                                   "error": "Usuario ya existe"})
        # Retorna mensaje de error en caso de que la validación de las contraseñas de como resultado False.
        return render(request, "registration/signup.html", {"form": UserCreationForm,
                                                            "error": "Las contraseñas no coinciden."})    


def log_in(request):
    if request.method == "GET":
        return render(request, "registration/login.html", {"form": AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "registration/login.html", {"form": AuthenticationForm,
                                                               "error": "Usuario o Contraseña incorrectas"})
        return render(request, "registration/login.html", {"form": AuthenticationForm})


def exit(request):
    """
    Funcion de logout del proyecto.
    """
    logout(request)
    return redirect("index")