# movies/models.py

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    poster_url = models.URLField()

    def __str__(self):
        return self.title
