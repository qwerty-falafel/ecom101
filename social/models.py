# social/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone

class UserProfilePost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
