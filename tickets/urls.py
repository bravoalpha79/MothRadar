from django.urls import path
from .views import TicketCreateView, TicketDetailView, TicketUpdateView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tickets/create/", TicketCreateView.as_view(), name="ticket-create"),
    path("tickets/<int:pk>/", TicketDetailView.as_view(), name="ticket-details"),
    path("tickets/edit/<int:pk>/", TicketUpdateView.as_view(), name="ticket-edit"),
]
