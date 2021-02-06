from django.db import models


class Author(models.Model):
    author_id = models.IntegerField(default='0')
    author_name = models.CharField(max_length=255, default='')
    born = models.CharField(max_length=255, default='')
    died = models.CharField(max_length=255, default='')
    work = models.CharField(max_length=255, default='')
    pic = models.CharField(max_length=2083, default='')
    bio = models.CharField(max_length=2083, default='')
    status = models.IntegerField(default='')
