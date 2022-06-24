# Create your models here.
import uuid

from django.db import models
from django.contrib.auth.models import User


class League(models.Model):
    SCORE_CHOICES = ((3, 3), (4, 4), (5, 5),)
    WINNER_CHOICES = ((1, 1), (2, 2), (3, 3),)
    TOP_CHOICES = ((1, 1), (2, 2), (3, 3),)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField('League Name', max_length=20, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.CharField('Logo', max_length=20, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    use_default_policy = models.BooleanField(default=True)
    policy_gs_90_min_score = models.IntegerField(default=3, choices=SCORE_CHOICES)
    policy_gs_90_min_winner = models.IntegerField(default=1, choices=WINNER_CHOICES)
    policy_no_90_min_score = models.IntegerField(default=3, choices=SCORE_CHOICES)
    policy_no_120_min_winner = models.IntegerField(default=1, choices=WINNER_CHOICES)
    policy_top_scorer = models.IntegerField(default=2, choices=TOP_CHOICES)
    policy_top_assist = models.IntegerField(default=2, choices=TOP_CHOICES)
    policy_best_team = models.IntegerField(default=2, choices=TOP_CHOICES)

    def __str__(self):
        return self.name
