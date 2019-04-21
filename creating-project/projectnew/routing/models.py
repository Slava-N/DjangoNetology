from django.db import models

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=256)


class Station(models.Model):
    name = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    routes = models.ManyToManyField(to=Route, related_name='stations')