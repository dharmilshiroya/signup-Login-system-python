from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    password2 = models.CharField(max_length=30)


