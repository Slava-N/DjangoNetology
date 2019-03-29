from django.db import models
from django.utils import text

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.TextField(default='')
    price = models.IntegerField(default=0)
    image = models.TextField(default='')
    release_date = models.DateField(default=0)
    lte_exists = models.TextField(default=False)
    slug = models.TextField(default='')
    pass
