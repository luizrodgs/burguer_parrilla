from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Order


def order_dashboard(request):
    orders = Order.objects.order_by("date")
    paginator = Paginator(orders, 30)
    page = request.GET.get("page")
    orders_per_page = paginator.get_page(page)
    package = {"orders": orders_per_page}
    return render(request, "orders/order_dashboard.html", package)


def get_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_to_show = {"order": order}
    return render(request, "orders/order.html", order_to_show)


def create_order(request):
    if request.method == "POST":
        name = request.POST["order_name"]
        phone = request.POST["order_phone"]
        address = request.POST["order_address"]
        order = Order.objects.create(name=name, phone=phone, address=address)
        order.save()
        return redirect("order_dashboard")
    else:
        return render(request, "orders/create_order.html")


def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return redirect("order_dashboard")


def edit_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_to_edit = {"order": order}
    return render(request, "orders/edit_order.html", order_to_edit)


def update_order(request):
    if request.method == "POST":
        order_id = request.POST["order_id"]
        order = Order.objects.get(pk=order_id)
        order.name = request.POST["order_name"]
        order.phone = request.POST["order_phone"]
        order.address = request.POST["order_address"]
        order.save()
    return redirect("order_dashboard")
