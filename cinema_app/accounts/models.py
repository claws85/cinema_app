
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models

from cinema_app.core.models import TimeStampedModel

from django_countries.fields import CountryField



class Customer(User):

    birthdate = models.DateField(
        auto_now_add=True,
        null=False
    )

    account = models.OneToOneField(
        'Account',
        on_delete=models.CASCADE
    )

    @property
    def calculate_age(self):
        delta = self.birthdate - datetime.today()
        return round(delta.days / 365, 0)

    # create dictionary for these options
    @property
    def allowed_certificate(self):
        age = self.calculate_age
        if age >= 18:
            return '18+'
        elif 15 >= age < 18:
            return '15'
        elif 12 >= age < 15:
            return '12'
        else:
            return 'U/PG'


class CustomerAddress(TimeStampedModel):

    customer = models.ForeignKey(
        'Customer',
        related_name="Addresses",
        on_delete=models.CASCADE
    )

    name = models.CharField(
        "Property name or number",
        max_length=100,
        blank=False
    )

    address1 = models.CharField(
        "Address line 1",
        max_length=300,
        blank=False
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=300,
    )

    postal_code = models.CharField(
        "UK postal code",
        max_length=20,
        blank=False
    )

    city = models.CharField(
        "City",
        max_length=100,
    )

    country = models.CharField(
        "Country",
        choices=CountryField()
    )


class Account(TimeStampedModel):

    film_club_activation_date = models.DateField()


    film_club_membership_expiry = models.DateField(
        default=datetime.now()+timedelta(days=365)
    )

    preference_info = models.OneToOneField(
        'CustomerPreferenceInfo',
        null=False
    )

    @property
    def membership_valid(self):
        if datetime.now() > self.film_club_membership_expiry:
            return False
        return True



class CustomerPreferenceInfo(TimeStampedModel):

    pass
    # implement when ready
    #preferred_genres = models.ManyToManyField(Genre)

    # films_viewed - a foreignkey to the films model (on the film model)

    # adult_customer = models.BooleanField(null=False)

