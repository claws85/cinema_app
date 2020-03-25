
import logging

from django.core.management.base import BaseCommand
from django.db import transaction

from cinema_app.screens.models import Screen, Seat


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        try:
            self.create_screens()

            self.create_seats()

        except Exception as e:
            logger.error("The following error was encountered during the "
                         "creation of the cinema screens and seats:\n"
                         "{}".format(e)
                         )

    def create_screens(self):
        """
        Creates the cinema's two screens, with
        100 seat capacity
        """
        if not Screen.objects.all():
            for num in range(1, 3):
                Screen.objects.create(
                    number=num,
                    capacity=100
                )
            self.stdout.write("Cinema screens created.\n")

    def create_seats(self):
        """
        Creates seats for each cinema screen,
        with 30 premium seats
        """
        seat_rows = ['A', 'B', 'C', 'D', 'E',
                     'F', 'G', 'H', 'I', 'J']

        premium_rows = {'H': 'H',
                        'I': 'I',
                        'J': 'J'}

        if not Seat.objects.all():

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
                                **kwargs
                            )
                self.stdout.write("Screen seats created.")
