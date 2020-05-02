from django.urls import path
from .views import TicketCreateView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tickets/create/", TicketCreateView.as_view(), name="ticket-create"),
]
