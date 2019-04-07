from django.db import models


class Topics(models.Model):

    title = models.CharField(max_length=256, verbose_name='Раздел')

    def __str__(self):
        return self.title

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    topics = models.ManyToManyField(Topics, through='TopicsLogs', related_name='topicsadded')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class TopicsLogs(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE)
    date_changed = models.DateField()
    primary_topic = models.BooleanField()


