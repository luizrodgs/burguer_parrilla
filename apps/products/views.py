from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Product


def item_dashboard(request):
    if request.user.is_authenticated:
        itens = Product.objects.order_by("name")
        paginator = Paginator(itens, 30)
        page = request.GET.get("page")
        items_per_page = paginator.get_page(page)
        package = {"items": items_per_page}
        return render(request, "items/item_dashboard.html", package)
    else:
        return redirect("index")

def get_item(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(Product, pk=item_id)
        item_to_show = {"item": item}
        return render(request, "items/item.html", item_to_show)
    else:
        return redirect("index")

def create_item(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST["item_name"]
            price = request.POST["item_price"]
            item = Product.objects.create(name=name, price=price)
            item.save()
            return redirect("item_dashboard")
        else:
            return render(request, "items/create_item.html")
    else:
        return redirect("index")

def delete_item(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(Product, pk=item_id)
        item.delete()
        return redirect("item_dashboard")
    else:
        return redirect("index")

def edit_item(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(Product, pk=item_id)
        item_to_edit = {"item": item}
        return render(request, "items/edit_item.html", item_to_edit)
    else:
        return redirect("index")

def update_item(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            item_id = request.POST["item_id"]
            item = Product.objects.get(pk=item_id)
            item.name = request.POST["item_name"]
            item.price = request.POST["item_price"]
            item.save()
        return redirect("item_dashboard")
    else:
        return redirect("index")
        