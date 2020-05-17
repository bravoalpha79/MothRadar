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
    """Handle upvoting of Bug tickets (payment-free)."""
    voter = request.user
    ticket = get_object_or_404(Ticket, pk=pk)
    upvoted = Upvote.objects.filter(ticket=ticket.id, upvoter=voter.id)

    # return error if user already upvoted the Ticket
    if upvoted:
        return JsonResponse({"error": "Already upvoted."})
    else:
        Upvote.objects.create(ticket_id=ticket.id, upvoter_id=voter.id)
        return JsonResponse({"success": "Upvote successful!"})


@login_required
def upvote_paid(request, pk):
    """
    Handle Stripe payment and upvoting of Feature tickets.
    Payment code adapted from course videos.
    """
    voter = request.user
    ticket = get_object_or_404(Ticket, pk=pk)
    upvoted = Upvote.objects.filter(ticket=ticket.id, upvoter=voter.id)

    PRICE = 10

    if request.method == "POST":
        form = UpvoteFeaturePaymentForm(request.POST)

        if form.is_valid():
            # if ticket already upvoted, return to Ticket details
            # without processing payment.
            if upvoted:
                messages.warning(
                    request,
                    ("Ticket already upvoted. "
                     "Your payment will not be processed.")
                )
                return redirect(reverse("ticket-details", args=[pk]))
            # otherwise, attempt Stripe payment
            else:
                try:
                    customer = stripe.Charge.create(
                        amount=int(PRICE * 100),
                        currency="EUR",
                        description=request.user.email,
                        card=form.cleaned_data["stripe_id"],
                    )
                    # payment successful - upvote ticket
                    # and redirect to Ticket details
                    if customer.paid:
                        Upvote.objects.create(ticket=ticket, upvoter=voter)
                        messages.success(
                            request,
                            ("Your payment was processed successfully! "
                             "Ticket upvoted.")
                        )
                        return redirect(reverse("ticket-details", args=[pk]))
                    # payment unsuccessful
                    else:
                        messages.error(request, "Unable to process payment")
                # handle Stripe exceptions
                except stripe.error.CardError:
                    messages.error(request, "Your card was declined!")
        # handle form errors
        else:
            print(form.errors)
            messages.warning(
                request, "Unable to process payment with that card.")

    else:
        form = UpvoteFeaturePaymentForm()

    return render(
        request,
        "upvotes/payment.html",
        {
            "form": form,
            "publishable": settings.STRIPE_PUBLISHABLE,
            "ticket": ticket
        },
    )
