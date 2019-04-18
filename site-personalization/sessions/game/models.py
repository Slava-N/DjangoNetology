from django.db import models

from datetime import datetime

class Player(models.Model):
    player_id = models.IntegerField(default=0)

class Game(models.Model):
    players = models.ManyToManyField(Player, through='PlayerGameInfo')
    secret_number = models.IntegerField(default=0)
    finished = models.BooleanField(default=False)
    game_id = models.IntegerField(default = 0)

class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, default=0)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default=0)
    guess = models.IntegerField(default=0)
    time = models.DateTimeField(default=datetime.now())

