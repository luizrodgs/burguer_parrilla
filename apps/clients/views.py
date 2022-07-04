from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Client


def client_dashboard(request):
    if request.user.is_authenticated:
        clients = Client.objects.order_by("name")
        paginator = Paginator(clients, 30)
        page = request.GET.get("page")
        clients_per_page = paginator.get_page(page)
        package = {"clients": clients_per_page}
        return render(request, "clients/client_dashboard.html", package)
    else:
        return redirect("index")

def get_client(request, client_id):
    if request.user.is_authenticated:
        client = get_object_or_404(Client, pk=client_id)
        client_to_show = {"client": client}
        return render(request, "clients/client.html", client_to_show)
    else:
        return redirect("index")

def create_client(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST["client_name"]
            phone = request.POST["client_phone"]
            address = request.POST["client_address"]
            client = Client.objects.create(name=name, phone=phone, address=address)
            client.save()
            return redirect("client_dashboard")
        else:
            return render(request, "clients/create_client.html")
    else:
        return redirect("index")

def delete_client(request, client_id):
    if request.user.is_authenticated:
        client = get_object_or_404(Client, pk=client_id)
        client.delete()
        return redirect("client_dashboard")
    else:
        return redirect("index")

def edit_client(request, client_id):
    if request.user.is_authenticated:
        client = get_object_or_404(Client, pk=client_id)
        client_to_edit = {"client": client}
        return render(request, "clients/edit_client.html", client_to_edit)
    else:
        return redirect("index")

def update_client(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            client_id = request.POST["client_id"]
            client = Client.objects.get(pk=client_id)
            client.name = request.POST["client_name"]
            client.phone = request.POST["client_phone"]
            client.address = request.POST["client_address"]
            client.save()
        return redirect("client_dashboard")
    else:
        return redirect("index")
