from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import OrderForm
from .models import Order, OrderProduct


def index(request):
    return render(request, "index.html")


def order_dashboard(request):
    if request.user.is_authenticated:
        orders = Order.objects.order_by("date")
        paginator = Paginator(orders, 30)
        page = request.GET.get("page")
        orders_per_page = paginator.get_page(page)
        package = {"orders": orders_per_page}
        return render(request, "orders/order_dashboard.html", package)
    else:
        return redirect("index")


def get_order(request, order_id):
    if request.user.is_authenticated:
        order = get_object_or_404(Order, pk=order_id)
        order_to_show = {"order": order}
        return render(request, "orders/order.html", order_to_show)
    else:
        return redirect("index")


def create_order(request):
    order_form = OrderForm(request.POST)
    context = {"order_form": order_form}
    if request.user.is_authenticated:
        if request.method == "POST":
            if order_form.is_valid():
                order = order_form.clean()
                Order.objects.create(
                    client_id=order["client"].first(),
                    obs=order["obs"],
                    date=order["date"],
                )
                OrderProduct.objects.create(
                    order_id=Order.objects.last(),
                    product_id=order["products"].first(),
                )
                return redirect("order_dashboard")
        return render(request, "orders/create_order.html", context)
    return redirect("index")


def delete_order(request, order_id):
    if request.user.is_authenticated:
        order = get_object_or_404(Order, pk=order_id)
        order.delete()
        return redirect("order_dashboard")
    else:
        return redirect("index")


def edit_order(request, order_id):
    if request.user.is_authenticated:
        order = get_object_or_404(Order, pk=order_id)
        order_to_edit = {"order": order}
        return render(request, "orders/edit_order.html", order_to_edit)
    else:
        return redirect("index")


def update_order(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            order_id = request.POST["order_id"]
            order = Order.objects.get(pk=order_id)
            order.name = request.POST["order_name"]
            order.phone = request.POST["order_phone"]
            order.address = request.POST["order_address"]
            order.save()
        return redirect("order_dashboard")
    else:
        return redirect("index")
