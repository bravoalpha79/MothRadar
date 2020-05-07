from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from .models import Comment

# The Comment.objects.create solution obtained from ckz8780
@login_required
def add_comment(request, pk):
    if request.method == "POST":
        text = request.POST.get("text")
        author = request.user
        ticket = get_object_or_404(Ticket, pk=pk)
        try:
            Comment.objects.create(text=text, author=author, rel_ticket=ticket)
            return JsonResponse(
                {
                    "success": "You comment was successfully added.",
                    "text": str(text),
                    "author": author.username,
                }
            )
        except:
            return JsonResponse({"error": "Something went wrong. Comment not added."})
