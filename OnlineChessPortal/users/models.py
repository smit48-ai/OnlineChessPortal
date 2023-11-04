from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import int_list_validator
from django.utils.crypto import get_random_string
# Create your models here.

class User(AbstractUser):
    Rating=models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to='profile_pics', default='default.jpg')
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True, null=True)

    def generate_verification_token(self):
        token = get_random_string(length=30)
        self.verification_token = token
        self.save()
        return token
    