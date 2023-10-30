from django.db import models
from django.conf import settings

class GameModel(models.Model):
    player1Id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='player_1')
    palyer2Id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='player_2')
    status=models.CharField(max_length=100, default="None")
