from django.db import models

# class User(models.Model):
#     user_name = models.CharField(max_length=50)
#     _password = models.CharField(max_length=30)


class Contact(models.Model):
    name = models.CharField(max_length=60)
    number = models.IntegerField()

    def __str__(self):
        return self.name, self.number