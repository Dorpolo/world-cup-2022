from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile


def createProfile(sender, instance, created: bool, **kwargs):
    print("Profile signal trigger")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name=user.username,
            email=user.email,
        )

    print('New Profile has been auto-generated')

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print('Deleting User...')

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
