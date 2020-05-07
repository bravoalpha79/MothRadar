from django.shortcuts import render, get_object_or_404

# Create your views here.
def upvote(request, pk):
    voter = request.user
    ticket = get_object_or_404(Ticket, pk=pk)
    try:
        Upvote.objects.get(ticket=ticket, author=voter)
        return JsonResponse({"text": "Already upvoted."})
    except:
        Upvote.objects.create(ticket=ticket, author=voter)
        return JsonResponse({"text": "Upvote successful!"})
