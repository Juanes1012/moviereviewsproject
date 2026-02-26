from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to='movie/images/', default='movie/images/default.jpg')

    def __str__(self):
        return self.title