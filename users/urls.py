from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.profile, name="profile"),
    path("update/", views.update_profile, name="update_profile"),
]
