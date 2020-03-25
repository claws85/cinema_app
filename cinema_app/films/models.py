from django.db import models

from cinema_app.core.models import TimeStampedModel
from cinema_app.films.utils import film_genres



class Genre(models.Model):

    name = models.CharField(
        max_length=15,
        choices=film_genres,
        unique=True,
    )

    def __str__(self):
        return "{}".format(
            self.name
        )


class Film(TimeStampedModel):

    genre = models.ManyToManyField(
        'Genre',
    )

    name = models.CharField(
        max_length=300
    )

    year = models.DateField()

    rating = models.CharField(
        max_length=10,
    )

    runtime = models.CharField(
        max_length=10,
    )

    description = models.CharField(
        max_length=500,
        blank=True,
    )

    metascore = models.CharField(
        max_length=5,
    )

    def __str__(self):
        return "{}, {}".format(
            self.name,
            self.year
        )


