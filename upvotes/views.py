from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from tickets.models import Ticket
from .models import Upvote

# Create your views here.
def upvote(request, pk):
    voter = request.user
    ticket = get_object_or_404(Ticket, pk=pk)
    try:
        Upvote.objects.get(ticket=ticket, upvoter=voter)
        return JsonResponse({"error": "Already upvoted."})
    except:
        Upvote.objects.create(ticket=ticket, upvoter=voter)
        return JsonResponse({"success": "Upvote successful!"})
