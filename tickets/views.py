from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Count
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from comments.models import Comment
from comments.forms import EditCommentForm
from upvotes.models import Upvote
from .models import Ticket


def home(request):
    """Render home page."""
    return render(request, "tickets/home.html")


@method_decorator(login_required, name="dispatch")
class TicketCreateView(CreateView):
    """
    Display ticket creation form and validate input data.
    If the form is valid, set the current user as ticket author
    and create the ticket.
    """

    model = Ticket
    fields = ["title", "description", "ticket_type"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TicketDetailView(DetailView):
    model = Ticket
    """
    Display detail view of the selected ticket,
    including upvote count and comments (if any).
    Disable Upvote button if current user already
    upvoted the ticket.
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        voter = self.request.user
        upvoted = Upvote.objects.filter(ticket=self.object.id, upvoter=voter.id)

        context["comments"] = Comment.objects.filter(
            rel_ticket=self.object.id
        ).order_by("created")
        context["upvotes"] = Upvote.objects.filter(ticket=self.object.id).count()

        if upvoted:
            context["uv_status"] = False
        else:
            context["uv_status"] = True

        return context


@method_decorator(login_required, name="dispatch")
class TicketUpdateView(UpdateView):
    """
    Display ticket update form and validate input data.
    """

    model = Ticket
    fields = ["title", "description", "ticket_type"]

    def get_queryset(self):
        queryset = super().get_queryset()
        author = self.request.user
        # Limit edit view access only to tickets created by the
        # current user - solution obtained from Stack Overflow.
        queryset = Ticket.objects.filter(author=author)
        return queryset


class TicketListView(ListView):
    """
    Display list of all tickets in the database, 
    search box and filter views sidebar.
    Display number of tickets created by the current user.
    Handle search box inputs.
    """

    paginate_by = 5
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["path"] = self.request.path
        if self.request.user.is_authenticated:
            context["user_ticket_count"] = Ticket.objects.filter(
                author=self.request.user
            ).count()
        return context

    # Search solution adapted from a post on Stack Overflow
    # using Django documentation.
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        # perform search if entered
        if search:
            queryset = queryset.filter(description__icontains=search)
        # otherwise display all tickets in the view
        else:
            queryset = queryset
        return queryset


class BugListView(TicketListView):
    """ 
    From all tickets, display only Bugs.
    """

    queryset = Ticket.objects.filter(ticket_type="BUG")


class FeatureListView(TicketListView):
    """ 
    From all tickets, display only Features.
    """

    queryset = Ticket.objects.filter(ticket_type="FEATURE")


class UpvoteSortedListView(TicketListView):
    """ 
    Display all tickets sorted by upvote count.
    Annotation method suggested by ckz8780.
    """

    queryset = Ticket.objects.annotate(votes=Count("upvotes")).order_by("-votes")


@method_decorator(login_required, name="dispatch")
class UserRaisedTicketView(TicketListView):
    """ 
    From all tickets, display only tickets raised
    by the current user.
    """

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Ticket.objects.filter(author=self.request.user)
        return queryset
