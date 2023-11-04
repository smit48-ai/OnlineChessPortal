from django.db import models
from django.conf import settings
from tournaments.models import Tournament

##do we need reference to users??
class GameModel(models.Model):
    player1Id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='player_1')
    player2Id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='player_2')
    winner=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='winner', null=True)
    position=models.CharField(max_length=100000,default="")
    status=models.CharField(max_length=100, default="running")
    # contest=models.ForeignKey(Tournament, on_delete=models.CASCADE,related_name='tournament',default=1)
