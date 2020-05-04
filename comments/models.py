from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.urls import reverse
from tickets.models import Ticket

# Create your models here.
class Comment(models.Model):
    text = models.TextField("Your comment")
    created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rel_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        entry = f"{self.author} // {self.rel_ticket} // {self.created}"
        return entry
