from django.db import models

class GameModel(models.Model):
    player1Id=models.BigIntegerField()
    palyer2Id=models.BigIntegerField()
    moves=models.CharField(max_length=10000)
    winner=models.BigIntegerField()
