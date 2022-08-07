from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import OrderForm
from .models import Order

def index(request):
    return render(request, "index.html")


@login_required
def order_dashboard(request):
    orders = Order.objects.order_by("date")
    paginator = Paginator(orders, 30)
    page = request.GET.get("page")
    orders_per_page = paginator.get_page(page)
    package = {"orders": orders_per_page}
    return render(request, "orders/order_dashboard.html", package)


@login_required
def get_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_to_show = {"order": order}
    return render(request, "orders/order.html", order_to_show)


@login_required
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                client_id=(form.cleaned_data.get("client")).all().last(),
                obs=form.cleaned_data.get("obs"),
                date=form.cleaned_data.get("date"),
            )
            for product in form.cleaned_data["products"]:
                order.products.add(product)
            return redirect("order_dashboard")
    else:
        form = OrderForm()
    return render(request, "orders/create_order.html", {"form": form})


@login_required
def delete_order(_, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return redirect("order_dashboard")


@login_required
def edit_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_to_edit = {"order": order}
    return render(request, "orders/edit_order.html", order_to_edit)


@login_required
def update_order(request):
    if request.method == "POST":
        order_id = request.POST["order_id"]
        order = Order.objects.get(pk=order_id)
        order.name = request.POST["order_name"]
        order.phone = request.POST["order_phone"]
        order.address = request.POST["order_address"]
        order.save()
    return redirect("order_dashboard")
