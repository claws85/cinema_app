from django.db import models

from cinema_app.accounts.models import Customer
from cinema_app.films.models import Film
from cinema_app.screens.models import Screen, Seat, ShowTime
from cinema_app.core.models import TimeStampedModel


class Ticket(TimeStampedModel):

    code = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        unique=True
    )

    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    seat = models.ForeignKey(
        Seat,
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    showtime = models.ForeignKey(
        ShowTime,
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    customer = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.SET_NULL,
    )

    sold = models.BooleanField(
        null=False,
        default=False,
    )


    def save(self, *args, **kwargs):
        if self._state.adding:
            self.code = '{}-{}-{}-{}'.format(
                self.film.name,
                self.showtime.screen.number,
                self.seat.seat_number,
                self.showtime.early_or_late
            )

        super(Ticket, self).save(self, *args, **kwargs)


