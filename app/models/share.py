__author__ = 'riegel'

from django.db import models


class Share(models.Model):
    name = models.CharField(max_length=60)
    wkn = models.CharField(max_length=30)