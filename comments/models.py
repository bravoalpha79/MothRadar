from django.db import models
from django.contrib.auth.models import User
from tickets.models import Ticket


class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="comments")
    rel_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        entry = f"{self.author} // {self.rel_ticket} // {self.created}"
        return entry
