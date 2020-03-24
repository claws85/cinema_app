from django.db import models

from cinema_app.core.models import TimeStampedModel
from cinema_app.films.utils import film_genres



class Genre(models.Model):

    name = models.CharField(
        choices=film_genres,
        blank=False,
        null=True
    )


class Film(TimeStampedModel):

    genre = models.ManyToManyField(
        Genre,
        on_delete=models.SET_NULL
    )

    name = models.CharField(
        blank=False,
        null=True
    )

    rating = models.CharField(
        max_length=10,
        blank=False,
        null=True
    )

    runtime = models.CharField(
        max_length=10,
    )

    description = models.CharField(
        max_length=500,
    )

    metascore = models.CharField(
        max_length=5,
        blank=False
    )


