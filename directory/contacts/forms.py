# from django import forms
from django.forms import ModelForm
from.models import Contact


# class CreateNewContact(forms.Form):
#     name = forms.CharField(label="Nombre y apellido contacto 🡒 ", max_length=200)
#     number = forms.IntegerField(label="Numero telefonico de contacto 🡒 ")


class CreateContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "number"]