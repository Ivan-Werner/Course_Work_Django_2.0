from django.urls import path

from client.apps import ClientConfig
from client.views import (
    ClientCreateView,
    ClientDeleteView,
    ClientDetailView,
    ClientListView,
    ClientUpdateView,
)

app_name = ClientConfig.name

urlpatterns = [
    path("communication/", ClientListView.as_view(), name="client_list"),
    path("communication/create/", ClientCreateView.as_view(), name="client_create"),
    path("communication/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path(
        "communication/<int:pk>/update/",
        ClientUpdateView.as_view(),
        name="client_update",
    ),
    path(
        "communication/<int:pk>/delete/",
        ClientDeleteView.as_view(),
        name="client_delete",
    ),
]
