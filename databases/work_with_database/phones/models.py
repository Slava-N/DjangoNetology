from django.db import models
from django.utils import text


class Phone(models.Model):

    # В файле models.py нашего приложения создаем модель
    # Phone с полями id, name, price, image, release_date,
    # lte_exists и slug. Поле id - должно быть основным ключом модели.

    # id = models.IntegerField(primary_key=True)
    # name = models.TextField(default='')
    # price = models.IntegerField(default=0)
    # image = models.TextField(default='')
    # release_date = models.DateField(default=0)
    # lte_exists = models.TextField(default=False)
    # # slug = models.TextField(default=text.slugify(name))
    pass
