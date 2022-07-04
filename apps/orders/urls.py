from django.urls import path

from .views import (
    create_order,
    delete_order,
    edit_order,
    get_order,
    index,
    order_dashboard,
    update_order,
)

urlpatterns = [
    path("", index, name="index"),
    path("pedidos/dashboard", order_dashboard, name="order_dashboard"),
    path("pedidos/<int:order_id>", get_order, name="get_order"),
    path("pedidos/criar", create_order, name="create_order"),
    path("pedidos/deletar/<int:order_id>", delete_order, name="delete_order"),
    path("pedidos/editar/<int:order_id>", edit_order, name="edit_order"),
    path("pedidos/atualizar", update_order, name="update_order"),
]
