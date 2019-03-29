from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    screen_size = models.IntegerField()
    anouncement_date = models.DateField()
    camera = models.IntegerField()
    bluetooth = models.TextField()
    ozu = models.IntegerField()
    url = models.TextField(default='beru.ru')



# name, price, screen_size, anouncement_date, camera, bluetooth, ozu
