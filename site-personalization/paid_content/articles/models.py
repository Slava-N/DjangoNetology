from django.contrib.auth.models import AbstractUser, User
from django.db import models
import django.utils.timezone as timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_subscription = models.BooleanField(default=False)


class Article(models.Model):
    title = models.CharField(max_length=256, default='Title')
    text = models.TextField(default='')
    caption = models.ImageField(default='default.jpg')
    commercial_article = models.BooleanField(default=False)
    submit_time = models.DateTimeField(default=timezone.now)
