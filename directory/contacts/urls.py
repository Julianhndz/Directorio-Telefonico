from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.contact_list, name="list"),
    path("logout/", views.exit, name="exit"),
]
