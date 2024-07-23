from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    telegram_chat_id = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
