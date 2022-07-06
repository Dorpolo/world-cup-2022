# Create your models here.
import uuid

from django.db import models
from django.contrib.auth.models import User

from users.models import Profile


class League(models.Model):
    SCORE_CHOICES = ((3, 3), (4, 4), (5, 5),)
    WINNER_CHOICES = ((1, 1), (2, 2), (3, 3),)
    TOP_CHOICES = ((1, 1), (2, 2), (3, 3),)

    id = models.AutoField(auto_created=True, primary_key=True, unique=True)
    name = models.CharField('League Name', max_length=20, unique=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    logo = models.ImageField('Logo', null=True, blank=True, default='default.png')
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


class LeagueMember(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, unique=True)
    nick_name = models.CharField('Nick Name', max_length=20, unique=True)
    profile_pic = models.ImageField('Profile Pic', null=True, blank=True, default='default.png')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
