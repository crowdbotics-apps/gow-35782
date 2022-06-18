from django.conf import settings
from django.db import models


class Buyer(models.Model):
    "Generated Model"
    buyer = models.BigIntegerField()
    address = models.BigIntegerField()
