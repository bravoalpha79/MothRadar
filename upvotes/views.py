from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.conf import settings
from tickets.models import Ticket
from .models import Upvote
from .forms import UpvoteFeaturePaymentForm
import stripe

# Create your views here.
@login_required
def upvote(request, pk):
    voter = request.user
    ticket = get_object_or_404(Ticket, pk=pk)
    try:
        Upvote.objects.get(ticket=ticket, upvoter=voter)
        return JsonResponse({"error": "Already upvoted."})
    except:
        Upvote.objects.create(ticket=ticket, upvoter=voter)
        return JsonResponse({"success": "Upvote successful!"})


@login_required
def upvote_paid(request, pk):

    stripe.api_key = settings.STRIPE_SECRET

    voter = request.user
    ticket = get_object_or_404(Ticket, pk=pk)

    PRICE = 10

    if request.method == "POST":
        form = UpvoteFeaturePaymentForm(request.POST)

        if form.is_valid():
            try:
                Upvote.objects.get(ticket=ticket, upvoter=voter)
                return messages.warning(
                    "Ticket already upvoted. Your payment will not be processed."
                )
                return redirect(reverse("ticket-details", pk=pk))
            except:
                try:
                    customer = stripe.Charge.create(
                        amount=int(PRICE * 100),
                        currency="EURO",
                        description=request.user.email,
                        card=form.cleaned_data["stripe_id"],
                    )
                except stripe.error.cardError:
                    messages.error(request, "Your card was declined!")

                if customer.paid:
                    Upvote.objects.create(ticket=ticket, upvoter=voter)
                    messages.success(
                        request,
                        "Your payment was processed successfully! Ticket upvoted.",
                    )
                    return redirect(reverse("ticket-details", pk=pk))
                else:
                    messages.error(request, "Unable to process payment")

        else:
            messages.error(request, "Unable to process payment with that card.")

    else:
        form = UpvoteFeaturePaymentForm()

    return render(request, "payment.html", {"form": form})
