from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

# Profile model created using Corey Schafer's YT tutorial
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
