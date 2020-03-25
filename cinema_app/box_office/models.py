from django.db import models

from cinema_app.core.models import TimeStampedModel


class Ticket(TimeStampedModel):

    code = models.CharField(
        null=False,
        blank=False,
        max_length=225,
        unique=True
    )

    film = models.ForeignKey(
        'films.Film',
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    seat = models.ForeignKey(
        'screens.Seat',
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    showtime = models.ForeignKey(
        'screens.ShowTime',
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    customer = models.ForeignKey(
        'accounts.Customer',
        null=True,
        on_delete=models.SET_NULL,
    )

    sold = models.BooleanField(
        null=False
    )

    def __str__(self):
        return "{}".format(
            self.film
        )

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.code = '{}-{}-{}-{}'.format(
                self.film.name.replace(' ', '').lower(),
                self.showtime.screen,
                self.seat.seat_number,
                self.showtime.early_or_late
            )

        super(Ticket, self).save(self, *args, **kwargs)
