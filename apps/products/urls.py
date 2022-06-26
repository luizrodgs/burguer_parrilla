from django.urls import path

from .views import (
    create_item,
    delete_item,
    edit_item,
    get_item,
    item_dashboard,
    update_item,
)

urlpatterns = [
    path("", item_dashboard, name="item_dashboard"),
    path("<int:item_id>", get_item, name="get_item"),
    path("criar", create_item, name="create_item"),
    path("deletar/<int:item_id>", delete_item, name="delete_item"),
    path("editar/<int:item_id>", edit_item, name="edit_item"),
    path("atualizar", update_item, name="update_item"),
]
