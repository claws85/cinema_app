import logging

from django.db import models, transaction

from cinema_app.box_office.models import Ticket
from cinema_app.core.models import TimeStampedModel


logger = logging.getLogger(__name__)


class Screen(TimeStampedModel):

    number = models.IntegerField(
        unique=True
    )

    capacity = models.IntegerField()

    def __str__(self):
        return "{}".format(
            self.number
        )

# move to films app?
class ShowTime(TimeStampedModel):

    time = models.DateTimeField()

    screen = models.ForeignKey(
        'Screen',
        on_delete=models.CASCADE
    )

    film = models.ForeignKey(
        'films.Film',
        on_delete=models.CASCADE
    )

    @property
    def early_or_late(self):
        if self.time.hour > 18:
            return 'late'
        return 'early'

    def __str__(self):
        return "{} Showtime".format(
            self.film
        )

    def save(self, *args, **kwargs):

        super(TimeStampedModel, self).save(self, *args, **kwargs)

        if self._state.adding:
            showtime = self.refresh_from_db()

            with transaction.atomic():
                try:
                    for seat in self.screen.seat_set.all():
                        Ticket.objects.create(
                            film=self.film,
                            seat=seat,
                            showtime=showtime
                        )
                except Exception as e:
                    logger.error("The following exception occurred while"
                                 " creating tickets for showtime '{}':\n"
                                 " '{}'".format(
                                     showtime,
                                     e
                                     )
                                 )

            logger.info("Tickets for {} in screen {} created.".
                        format(
                               self.film,
                               self.screen
                               )
                        )


class Seat(TimeStampedModel):

    screen = models.ForeignKey(
        'Screen',
        on_delete=models.CASCADE
    )

    seat_number = models.CharField(
        max_length=4
    )

    premium = models.BooleanField(
        default=False
    )

    def __str__(self):
        return "{}, screen {}".format(
            self.seat_number,
            self.screen
        )
