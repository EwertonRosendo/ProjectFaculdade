from django.db import models


# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    long = models.CharField(max_length=50)

    def __str__(self):
        return self.city


