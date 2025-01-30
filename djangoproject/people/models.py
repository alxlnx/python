from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30, default='')
    age = models.IntegerField(default=0)
    group = models.CharField(max_length=30, default='')
    fav_manufacturer = models.CharField(max_length=30, default='')