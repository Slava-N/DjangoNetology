from django.db import models

# Create your models here.

class Table_setup(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=256)
    width = models.IntegerField()
    version = models.IntegerField(default=0)

class Path_to_file(models.Model):
    choosen_path = models.FilePathField(path='/content_files/')

    def __str__(self):
        return self.choosen_path

    def get_path(self):
        return self.choosen_path

    def set_path(self, path):
        self.pk = 1
        self.choosen_path = path
        self.save()
        return None
