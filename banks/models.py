from django.db import models

# Create your models here.
class Bank(models.Model):
    """Model definition for Bank."""

    ifsc = models.CharField(max_length=15)
    bank_id = models.CharField(max_length=5)
    branch = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Bank."""

        verbose_name = "Bank"
        verbose_name_plural = "Banks"

