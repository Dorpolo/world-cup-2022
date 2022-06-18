from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class League(models.Model):
    league_name = models.CharField('League Name', max_length=20, unique=True)
    league_owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.league_name
