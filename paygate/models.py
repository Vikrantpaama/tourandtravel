from __future__ import unicode_literals
from django.db import models

import sqlite3

# Create your models here.
class book(models.Model):
    booking_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)

    packagename = models.CharField(max_length=20)
    amount = models.CharField(max_length=10)

class fbook(models.Model):
    booking_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    packagename = models.CharField(max_length=20)
    amount = models.CharField(max_length=10)



class hotelbook(models.Model):
    booking_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    hotelname=models.CharField(max_length=10)
    address = models.CharField(max_length=200, null=True)
    amount = models.CharField(max_length=10)


class airbook(models.Model):
    booking_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    Phone = models.CharField(max_length=50)
    Address = models.CharField(max_length=200)
    Address2 = models.CharField(max_length=200)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    trip_type = models.CharField(max_length=20)
    from1 = models.CharField(max_length=20)
    to = models.CharField(max_length=20)
    depart_on = models.DateField()
    Adult = models.CharField(max_length=30)
    Children = models.CharField(max_length=30)
    infact = models.CharField(max_length=30)
    class1 = models.CharField(max_length=30)


