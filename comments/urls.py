from django.urls import path
from . import views

urlpatterns = [
    path("comments/add/", views.add_comment, name="add-comment"),
    # path("comments/<int_pk>/edit", views.edit_comment, name="edit-comment"),
    # path("comments/<int_pk>/update", views.edit_comment, name="update-comment"),
    # path("comments/<int_pk>/delete", views.edit_comment, name="delete-comment"),
]
