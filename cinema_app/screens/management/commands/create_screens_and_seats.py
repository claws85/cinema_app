
import logging

from django.core.management.base import BaseCommand
from django.db import transaction

from cinema_app.screens.models import Screen, Seat


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        try:
            create_screens()
            self.stdout.write("Cinema screens created.\n")

            create_seats()
            self.stdout.write("Screen seats created.")

        except:
            logger.error("An error was encountered during the "
                         "creation of the cinema screens and seats")


def create_screens():
    """
    Creates the cinema's two screens, with
    100 seat capacity
    """

    for num in range(1, 3):
        Screen.objects.create(
            number=num,
            capacity=100
        )


def create_seats():
    """
    Creates seats for each cinema screen,
    with 30 premium seats
    """
    seat_rows = ['A', 'B', 'C', 'D', 'E',
                 'F', 'G', 'H', 'I', 'J']

    premium_rows = {'H': 'H',
                    'I': 'I',
                    'J': 'J'}

    with transaction.atomic():
        for screen in Screen.objects.all():
            for row in seat_rows:
                for num in range(1, 11):
                    kwargs = {
                        'screen': screen,
                        'seat_number': row+'-'+str(num),
                    }
                    if premium_rows.get(row):
                        kwargs['premium'] = True

                    Seat.objects.create(
                        *kwargs
                    )
