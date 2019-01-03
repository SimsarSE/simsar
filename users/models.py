from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from star_ratings.models import AbstractBaseRating


class CustomUser(AbstractUser):
    GSM = PhoneNumberField(unique=True, blank=False)

    def __str__(self):
        return self.email