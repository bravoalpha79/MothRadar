from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.contrib.auth.decorators import login_required
from .models import Ticket

# Create your views here.
def home(request):
    return render(request, "tickets/home.html", {"title": "Homepage"})


class TicketCreateView(CreateView):
    model = Ticket
    fields = ["title", "description", "ticket_type"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TicketDetailView(DetailView):
    model = Ticket


class TicketUpdateView(UpdateView):
    model = Ticket
    fields = ["title", "description", "ticket_type"]


class TicketDeleteView(DeleteView):
    model = Ticket
    success_url = reverse_lazy("ticket-list")


class TicketListView(ListView):
    model = Ticket
