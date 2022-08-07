from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClientForm
from .models import Client


@login_required(login_url="login")
def client_dashboard(request):
    clients = Client.objects.order_by("name")
    paginator = Paginator(clients, 30)
    page = request.GET.get("page")
    clients_per_page = paginator.get_page(page)
    package = {"clients": clients_per_page}
    return render(request, "clients/client_dashboard.html", package)


@login_required(login_url="login")
def get_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client_to_show = {"client": client}
    return render(request, "clients/client.html", client_to_show)


@login_required(login_url="login")
def create_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("client_dashboard")
    form = ClientForm()
    return render(request, "clients/create_client.html", {"form": form})


@login_required(login_url="login")
def delete_client(_, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    return redirect("client_dashboard")


@login_required(login_url="login")
def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client_to_edit = {"client": client}
    return render(request, "clients/edit_client.html", client_to_edit)


@login_required(login_url="login")
def update_client(request):
    if request.method == "POST":
        client_id = request.POST["client_id"]
        client = Client.objects.get(pk=client_id)
        client.name = request.POST["client_name"]
        client.phone = request.POST["client_phone"]
        client.address = request.POST["client_address"]
        client.save()
    return redirect("client_dashboard")
