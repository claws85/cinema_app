
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models

from cinema_app.accounts.utils import certificate_age_ranges
from cinema_app.core.models import TimeStampedModel
from cinema_app.films.models import Film, Genre

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

    @property
    def allowed_certificate(self):
        age = self.calculate_age
        for _range in certificate_age_ranges:
            lower, upper = _range[0]
            if lower >= age < upper:
                return _range[2]

    @property
    def senior_member(self):
        if self.calculate_age < 60:
            return False
        return True


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

    street = models.CharField(
        "Street address",
        max_length=300,
        blank=False
    )

    city = models.CharField(
        "City",
        max_length=100,
    )

    county = models.CharField(
        "County",
        max_length=300,
        blank=False
    )

    postal_code = models.CharField(
        "Postal code",
        max_length=20,
        blank=False
    )

    country = models.CharField(
        "Country",
        choices=CountryField()
    )


class Account(TimeStampedModel):

    film_club_membership = models.OneToOneField(
        'FilmClubSubscription',
        null=True,
        on_delete=models.SET_NULL
    )

    preference_info = models.OneToOneField(
        'CustomerPreferenceInfo',
        null=True,
        on_delete=models.SET_NULL
    )


class CustomerPreferenceInfo(TimeStampedModel):

    preferred_genres = models.ManyToManyField(
        Genre,
        null=True,
        on_delete=models.SET_NULL
    )

    films_viewed = models.ManyToManyField(
        Film,
        null=True,
        on_delete=models.SET_NULL
    )


class FilmClubSubscription(TimeStampedModel):

    film_club_membership_expiry = models.DateField(
        default=datetime.now() + timedelta(days=365)
    )

    @property
    def membership_valid(self):
        if datetime.now() > self.film_club_membership_expiry:
            return False
        return True
