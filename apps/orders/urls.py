from django.urls import path

from .views import (
    create_order,
    delete_order,
    edit_order,
    get_order,
    order_dashboard,
    update_order,
)

urlpatterns = [
    path("", order_dashboard, name="order_dashboard"),
    path("<int:order_id>", get_order, name="get_order"),
    path("criar", create_order, name="create_order"),
    path("deletar/<int:order_id>", delete_order, name="delete_order"),
    path("editar/<int:order_id>", edit_order, name="edit_order"),
    path("atualizar", update_order, name="update_order"),
]
