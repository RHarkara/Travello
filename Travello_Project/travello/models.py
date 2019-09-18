from django.db import models

# Create your models here.

class Destination(models.Model):
    id : int
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class WarangalDetails(models.Model):
    id: int
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    new = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)