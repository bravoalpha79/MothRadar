from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.urls import reverse

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    BUG = "BUG"
    FEAT = "FEAT"
    TICKET_TYPE_CHOICES = [(BUG, "Bug"), (FEAT, "Feature")]
    ticket_type = models.CharField(
        max_length=4, choices=TICKET_TYPE_CHOICES, default=BUG
    )
    OPEN = "OPN"
    INPROG = "INP"
    CLO = "SOL"
    TICKET_STATUS_CHOICES = [(OPEN, "Opened"), (INPROG, "In progress"), (CLO, "Solved")]
    status = models.CharField(max_length=3, choices=TICKET_STATUS_CHOICES, default=OPEN)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ticket-details", kwargs={"pk": self.pk})
