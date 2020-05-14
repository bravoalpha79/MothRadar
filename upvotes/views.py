from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse
from django.conf import settings
from tickets.models import Ticket
from .models import Upvote
from .forms import UpvoteFeaturePaymentForm
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required
def upvote(request, pk):
    voter = request.user
    ticket = get_object_or_404(Ticket, pk=pk)
    upvoted = Upvote.objects.filter(ticket=ticket.id, upvoter=voter.id)

    if upvoted:
        return JsonResponse({"error": "Already upvoted."})
    else:
        Upvote.objects.create(ticket_id=ticket.id, upvoter_id=voter.id)
        return JsonResponse({"success": "Upvote successful!"})


@login_required
def upvote_paid(request, pk):

    voter = request.user
    ticket = get_object_or_404(Ticket, pk=pk)
    upvoted = Upvote.objects.filter(ticket=ticket.id, upvoter=voter.id)

    PRICE = 10

    if request.method == "POST":
        form = UpvoteFeaturePaymentForm(request.POST)
        print(voter, ticket)

        if form.is_valid():
            if upvoted:
                messages.warning(
                    request,
                    "Ticket already upvoted. Your payment will not be processed.",
                )
                return redirect(reverse("ticket-details", args=[pk]))
            else:
                try:
                    customer = stripe.Charge.create(
                        amount=int(PRICE * 100),
                        currency="EUR",
                        description=request.user.email,
                        card=form.cleaned_data["stripe_id"],
                    )

                    if customer.paid:
                        Upvote.objects.create(ticket=ticket, upvoter=voter)
                        messages.success(
                            request,
                            "Your payment was processed successfully! Ticket upvoted.",
                        )
                        return redirect(reverse("ticket-details", args=[pk]))
                    else:
                        messages.error(request, "Unable to process payment")

                except stripe.error.CardError:
                    messages.error(request, "Your card was declined!")

        else:
            print(form.errors)
            messages.warning(request, "Unable to process payment with that card.")

    else:
        form = UpvoteFeaturePaymentForm()

    return render(
        request,
        "upvotes/payment.html",
        {"form": form, "publishable": settings.STRIPE_PUBLISHABLE, "ticket": ticket},
    )
