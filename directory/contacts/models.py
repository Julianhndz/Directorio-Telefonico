from django.db import models
from django.contrib.auth.models import User

"""
Modelo de tabla intermedia para la relación muchos a muchos entre modelo User y modelo Contact
"""
class ContactUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ForeignKey("Contact", on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=60)
    number = models.IntegerField()
    users = models.ManyToManyField(User, through=ContactUser)

    def __str__(self):
        return self.name