from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreateCommentForm
from tickets.models import Ticket
from .models import Comment

# Create your views here.


@login_required
def add_comment(request, pk):
    if request.method == "POST":
        text = request.POST.get("text")
        author = request.user
        ticket = get_object_or_404(Ticket, pk=pk)
        Comment.objects.create(text=text, author=author, rel_ticket=ticket)
    return JsonResponse({"text": str(text), "author": author.username})
