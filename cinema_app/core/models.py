from django.db import models


class TimeStampedModel(models.Model):
    """An abstract base class for all our models,
    including 'created' and 'modified' fields"""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True