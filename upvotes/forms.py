from django import forms


class UpvoteFeaturePaymentForm(forms.Form):
    """Stripe Credit Card Payment form"""

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2030)]

    credit_card_number = forms.CharField(label="Credit Card number",
                                         required=False)
    cvv = forms.CharField(label="Security Code (CVV)", required=False)
    expiry_month = forms.ChoiceField(
        label="Expiry month", choices=MONTH_CHOICES, required=False
    )
    expiry_year = forms.ChoiceField(
        label="Expiry year", choices=YEAR_CHOICES, required=False
    )
    stripe_id = forms.CharField(widget=forms.HiddenInput)
