from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class User(AbstractUser):
    pass


class Message(models.Model):
    user = models.ForeignKey(
        User, blank=False, on_delete=models.CASCADE, related_name="msg_send"
    )
    receiver = models.ForeignKey(
        User, blank=False, on_delete=models.CASCADE, related_name="msg_receiver"
    )
    message = models.TextField(max_length=100)
    date_time = models.DateTimeField(default=now, editable=False)
