from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def create_user(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if empty_field(name):
            return redirect("create_user")
        if empty_field(email):
            return redirect("create_user")
        if password_dont_match(password, password2):
            return redirect("create_user")
        if User.objects.filter(email=email).exists():
            return redirect("create_user")
        if User.objects.filter(username=name).exists():
            return redirect("create_user")
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        return redirect("login")
    else:
        return render(request, "users/create_user.html")

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if empty_field(email) or empty_field(password):
            return render(request, "usuarios/login.html")
        if User.objects.filter(email=email).exists():
            name = User.objects.filter(email=email).values_list("username", flat=True).get()
            user = auth.authenticate(request, username=name, password=password)
            if user is not None:
                auth.login(request, user)
                print("Login realizado com sucesso")
                return redirect("/")
    return render(request, "users/login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def empty_field(field):
    return not field.strip()

def password_dont_match(password, password2):
    return password != password2
