from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import int_list_validator

# Create your models here.

class User(AbstractUser):
    Rating=models.IntegerField()
    # games=models.CharField(validators=int_list_validator)