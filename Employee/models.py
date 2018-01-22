from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Vacation(models.Model):
    employee = models.ForeignKey(User)
    description = models.CharField(max_length=100)
    fromdate = models.DateField()
