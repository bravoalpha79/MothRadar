from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(
                request, "Your account has been created, {}.".format(username)
            )
            form.save()
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})
