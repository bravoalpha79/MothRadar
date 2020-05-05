from django.urls import path
from .views import (
    TicketListView,
    TicketDetailView,
    TicketCreateView,
    TicketUpdateView,
    TicketDeleteView,
)
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tickets/", TicketListView.as_view(), name="ticket-list"),
    path("tickets/create/", TicketCreateView.as_view(), name="ticket-create"),
    path("tickets/<int:pk>/", TicketDetailView.as_view(), name="ticket-details"),
    path("tickets/<int:pk>/edit/", TicketUpdateView.as_view(), name="ticket-edit"),
    path("tickets/<int:pk>/delete/", TicketDeleteView.as_view(), name="ticket-delete"),
]
