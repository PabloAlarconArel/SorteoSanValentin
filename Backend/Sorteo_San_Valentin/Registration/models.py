from django.db import models
from django.contrib.auth.models import AbstractUser

class Registration(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return self.email







# Create your models here.
