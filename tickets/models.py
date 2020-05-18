from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Ticket(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="raised_tickets"
    )
    BUG = "BUG"
    FEAT = "FEATURE"
    TICKET_TYPE_CHOICES = [(BUG, "Bug"), (FEAT, "Feature")]
    ticket_type = models.CharField(
        max_length=7, choices=TICKET_TYPE_CHOICES, default=BUG
    )
    OPENED = "OPENED"
    INPROG = "INPROG"
    CLOSED = "SOLVED"
    TICKET_STATUS_CHOICES = [
        (OPENED, "Opened"),
        (INPROG, "In progress"),
        (CLOSED, "Solved"),
    ]
    status = models.CharField(
        max_length=6, choices=TICKET_STATUS_CHOICES, default=OPENED
    )

    def __str__(self):
        return "{} | {} | {} | {}".format(
            self.ticket_type, self.author, self.status, self.title)

    def get_absolute_url(self):
        return reverse("ticket-details", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-date_created"]
