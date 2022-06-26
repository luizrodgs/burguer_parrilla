from django.urls import path

from .views import (
    client_dashboard,
    create_client,
    delete_client,
    edit_client,
    get_client,
    update_client,
)

urlpatterns = [
    path("", client_dashboard, name="client_dashboard"),
    path("<int:client_id>", get_client, name="client_id"),
    # path("buscar", search, name="search"),
    path("criar", create_client, name="create_client"),
    path("deletar/<int:client_id>", delete_client, name="delete_client"),
    path("editar/<int:client_id>", edit_client, name="edit_client"),
    path("atualizar", update_client, name="update_client"),
]
