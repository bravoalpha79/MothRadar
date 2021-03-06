from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm


def register(request):
    """ Handle registration of new users. """
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                "Your account has been created, {}.".format(username)
            )
            form.save()
            return redirect("login")
    else:
        if request.user.is_authenticated:
            return redirect("home")
        else:
            form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    """ Display logged-in user's profile page. """
    return render(request, "users/profile.html")


@login_required
def update_profile(request):
    """ Handle updating of user's profile info. """
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your profile has been updated, {}.".format(
                    request.user.username),
            )
            return redirect("profile")
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "users/profile_update.html", {"form": form})
