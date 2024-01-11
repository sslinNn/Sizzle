from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=60)
    length = models.IntegerField(null=True)
    genre = models.ManyToManyField(Genre)
    description = models.TextField()
    release_date = models.DateField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return f'{self.title} - {self.release_date}'
