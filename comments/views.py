from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import CreateCommentForm
from tickets.models import Ticket

# Create your views here.
def add_comment(request, pk):
    if request.method == "POST":
        form = CreateCommentForm(request.POST)
        form.instance.author = request.user
        form.instance.rel_ticket = get_object_or_404(Ticket, pk=pk)
        if form.is_valid:
            form.save()
        return HttpResponse("Success!!")
