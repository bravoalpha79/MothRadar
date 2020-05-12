from django.urls import path, include
from .views import (
    TicketListView,
    TicketDetailView,
    TicketCreateView,
    TicketUpdateView,
    TicketDeleteView,
    BugListView,
    FeatureListView,
    UpvoteSortedListView,
)
from . import views

urlpatterns = [
    path("tickets/", TicketListView.as_view(), name="ticket-list"),
    path("tickets/bugs/", BugListView.as_view(), name="bug-list"),
    path("tickets/features/", FeatureListView.as_view(), name="feature-list"),
    path("tickets/sort-upvoted/", UpvoteSortedListView.as_view(), name="upvoted-list"),
    path("tickets/create/", TicketCreateView.as_view(), name="ticket-create"),
    path("tickets/<int:pk>/", include("comments.urls")),
    path("tickets/<int:pk>/", include("upvotes.urls")),
    path(
        "tickets/<int:pk>/details",
        TicketDetailView.as_view(template_name="upvotes/upvotes.html"),
        name="ticket-details",
    ),
    path("tickets/<int:pk>/edit/", TicketUpdateView.as_view(), name="ticket-edit"),
    path("tickets/<int:pk>/delete/", TicketDeleteView.as_view(), name="ticket-delete"),
    path("", views.home, name="home"),
]
