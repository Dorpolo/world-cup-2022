import uuid

from django.db import models


# Create your models here.
class GroupStageResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=100)
