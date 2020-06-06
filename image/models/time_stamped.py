from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    """
    This model defines the time stamping.
    """

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def get_created_time(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']
