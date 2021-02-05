from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=255)
    bio = models.CharField(max_length=2083)
    status = models.IntegerField()
