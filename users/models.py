from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    image = models.ImageField(default='profiles/default.png', null=True, blank=True, upload_to='profiles/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)
