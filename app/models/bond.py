__author__ = 'riegel'

from django.db import models
from share import Share


class Value(models.Model):
    name = models.CharField(max_length=60)
    wkn = models.CharField(max_length=30)
    share = models.ForeignKey(Share, verbose_name="")