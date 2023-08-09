from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.log_in, name="login"),
    path("list/", views.contact_list, name="list"),
    path("logout/", views.exit, name="exit"),
    path("create_contact/", views.create_contact, name="create"),
]
