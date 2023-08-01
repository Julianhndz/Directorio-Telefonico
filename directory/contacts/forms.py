from django import forms

class CreateNewContact(forms.Form):
    name = forms.CharField(label="Nombre y apellido contacto 🡒 ", max_length=200)
    number = forms.IntegerField(label="Numero telefonico de contacto 🡒 ")