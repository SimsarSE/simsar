from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GSM = PhoneNumberField(unique=True, blank=False)

    def __str__(self):
        return self.email
