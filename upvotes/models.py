from django.db import models
from django.contrib.auth.models import User
from tickets.models import Ticket

# Create your models here.
class Upvote(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    upvoter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        entry = f"{self.ticket} // {self.upvoter}"
        return entry
