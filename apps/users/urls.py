from django.urls import path

from . import views

urlpatterns = [
    path("cadastro", views.create_user, name="create_user"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]
