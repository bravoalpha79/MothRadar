from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from comments.models import Comment
from comments.forms import CreateCommentForm, EditCommentForm
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


# # method created with the help of https://djangocentral.com/creating-comments-system-with-django/
# def detail(request, pk):
#     ticket = get_object_or_404(Ticket, id=pk)
#     form = CreateCommentForm()
#     comments = Comment.objects.filter(rel_ticket=ticket).order_by("-created")

#     if request.method == "POST":
#         form = CreateCommentForm(request.POST)
#         form.instance.author = request.user
#         form.instance.rel_ticket = ticket
#         if form.is_valid():
#             form.save()
#             return redirect("ticket-details", pk)

#     return render(
#         request,
#         "tickets/ticket_detail.html",
#         {"ticket": ticket, "form": form, "comments": comments,},
#     )


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
