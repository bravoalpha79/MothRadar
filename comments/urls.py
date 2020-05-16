from django.urls import path
from . import views

urlpatterns = [
    path("comments/add/", views.add_comment, name="add-comment"),
]
