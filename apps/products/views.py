from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Item


def item_dashboard(request):
    itens = Item.objects.order_by("name")
    paginator = Paginator(itens, 30)
    page = request.GET.get("page")
    items_per_page = paginator.get_page(page)
    package = {"itens": items_per_page}
    return render(request, "items/item_dashboard.html", package)


def get_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item_to_show = {"item": item}
    return render(request, "items/item.html", item_to_show)


def create_item(request):
    if request.method == "POST":
        name = request.POST["item_name"]
        price = request.POST["item_price"]
        item = Item.objects.create(name=name, price=price)
        item.save()
        return redirect("item_dashboard")
    else:
        return render(request, "items/create_item.html")


def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return redirect("item_dashboard")


def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item_to_edit = {"item": item}
    return render(request, "items/edit_item.html", item_to_edit)


def update_item(request):
    if request.method == "POST":
        item_id = request.POST["item_id"]
        item = Item.objects.get(pk=item_id)
        item.name = request.POST["item_name"]
        item.price = request.POST["item_price"]
        item.save()
    return redirect("item_dashboard")
