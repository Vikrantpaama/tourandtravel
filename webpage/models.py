from __future__ import unicode_literals
from django.db import models
import sqlite3
# Create your models here.
class employees(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    age=models.IntegerField()
    salary = models.IntegerField()
    profilePicture=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.firstname




class videos(models.Model):
    title=models.CharField(max_length=15)
    description=models.TextField()
    album=models.CharField(max_length=20)
    extra=models.CharField(max_length=20)
    offer=models.BooleanField(default=False)
    cont=models.ImageField(upload_to='pics')
    videofile = models.FileField(upload_to='videos', null=True, verbose_name="video_file")



class package(models.Model):
    packagename = models.CharField(max_length=40)
    suitablegroup = models.CharField(max_length=40)
    image = models.ImageField(upload_to='pics')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    image1 = models.ImageField(upload_to='pics',null=True)
    name1 = models.CharField(max_length=40 ,null=True)
    lengthofstay1 = models.IntegerField(null=True)
    description1 = models.CharField(max_length=20000 ,null=True)
    location1 = models.CharField(max_length=200 ,null=True)
    image2 = models.ImageField(upload_to='pics' ,null=True)
    name2 = models.CharField(max_length=40 ,null=True)
    lengthofstay2 = models.IntegerField(null=True)
    description2 = models.CharField(max_length=20000 ,null=True)
    location2 = models.CharField(max_length=200 ,null=True)
    image3 = models.ImageField(upload_to='pics' ,null=True)
    name3 = models.CharField(max_length=40 ,null=True)
    lengthofstay3 = models.IntegerField(null=True)
    description3 = models.CharField(max_length=20000 ,null=True)
    location3 = models.CharField(max_length=200 ,null=True)
    def __str__(self):
        return self.packagename


class holidayspackage(models.Model):
    packagename = models.CharField(max_length=40)
    suitablegroup = models.CharField(max_length=40)
    image = models.ImageField(upload_to='pics')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    image1 = models.ImageField(upload_to='pics',null=True)
    name1 = models.CharField(max_length=40 ,null=True)
    lengthofstay1 = models.IntegerField(null=True)
    description1 = models.CharField(max_length=20000 ,null=True)
    location1 = models.CharField(max_length=200 ,null=True)
    image2 = models.ImageField(upload_to='pics' ,null=True)
    name2 = models.CharField(max_length=40 ,null=True)
    lengthofstay2 = models.IntegerField(null=True)
    description2 = models.CharField(max_length=20000 ,null=True)
    location2 = models.CharField(max_length=200 ,null=True)
    image3 = models.ImageField(upload_to='pics' ,null=True)
    name3 = models.CharField(max_length=40 ,null=True)
    lengthofstay3 = models.IntegerField(null=True)
    description3 = models.CharField(max_length=20000 ,null=True)
    location3 = models.CharField(max_length=200 ,null=True)
    def __str__(self):
        return self.packagename
class test(models.Model):
    packagename = models.CharField(max_length=40)
    suitablegroup = models.CharField(max_length=40)
    image = models.ImageField(upload_to='pics')
    amount = models.CharField(max_length=5)
    duration = models.IntegerField()
    image1 = models.ImageField(upload_to='pics',null=True)
    name1 = models.CharField(max_length=40 ,null=True)
    lengthofstay1 = models.IntegerField(null=True)
    description1 = models.CharField(max_length=20000 ,null=True)
    location1 = models.CharField(max_length=200 ,null=True)
    image2 = models.ImageField(upload_to='pics' ,null=True)
    name2 = models.CharField(max_length=40 ,null=True)
    lengthofstay2 = models.IntegerField(null=True)
    description2 = models.CharField(max_length=20000 ,null=True)
    location2 = models.CharField(max_length=200 ,null=True)
    image3 = models.ImageField(upload_to='pics' ,null=True)
    name3 = models.CharField(max_length=40 ,null=True)
    lengthofstay3 = models.IntegerField(null=True)
    description3 = models.CharField(max_length=20000 ,null=True)
    location3 = models.CharField(max_length=200 ,null=True)
    def __str__(self):
        return self.packagename

class hotel(models.Model):
    hotelname=models.CharField(max_length=10)
    image1 = models.ImageField(upload_to='pics')
    image2 = models.ImageField(upload_to='pics')
    image3 = models.ImageField(upload_to='pics')
    image4 = models.ImageField(upload_to='pics')
    address = models.CharField(max_length=200, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=12, null=True)
    WiFifacility = models.CharField(max_length=12, null=True)
    star = models.CharField(max_length=30)

    def __str__(self):
        return self.hotelname

class popular(models.Model):
    packagename = models.CharField(max_length=40)
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.packagename