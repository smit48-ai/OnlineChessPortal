from django.db import models

# Create your models here.


class Tournament(models.Model):
    Name=models.CharField(max_length=200)
    users=models.CharField(max_length=10000,null=True)
    gameIds=models.CharField(max_length=10000,null=True)
    status=models.CharField(max_length=100)