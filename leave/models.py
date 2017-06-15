from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    leave_remaining = models.IntegerField(default=0)

class Leave(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    leave_days = models.IntegerField()
    status = models.IntegerField(default="new")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)