from django.db import models

from cinema_app.films.models import Film
from cinema_app.core.models import TimeStampedModel


class Screen(TimeStampedModel):

    number = models.IntegerField(
        null=False
    )

    capacity = models.IntegerField(
        null=False
    )

# move to films app?
class ShowTime(TimeStampedModel):

    time = models.DateTimeField()

    screen = models.ForeignKey(
        'Screen',
        on_delete=models.CASCADE
    )

    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE
    )

    @property
    def early_or_late(self):
        if self.time.hour > 18:
            return 'late'
        return 'early'



class Seat(TimeStampedModel):

    screen = models.ForeignKey(
        'Screen',
        on_delete=models.CASCADE
    )

    seat_number = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )

    premium = models.BooleanField(
        default=False
    )



