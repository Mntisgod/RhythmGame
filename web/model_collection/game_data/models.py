from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    mail_address = models.EmailField(unique=True)


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    composer_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255, unique=True)


class Chart(models.Model):
    chart_id = models.AutoField(primary_key=True)
    chart_designer = models.CharField(max_length=255)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=255)


class PlayData(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    chart_id = models.ForeignKey(Chart, on_delete=models.CASCADE) # Assuming chart_id is an integer
    best_score = models.IntegerField()
    favorites = models.BooleanField(default=False)


