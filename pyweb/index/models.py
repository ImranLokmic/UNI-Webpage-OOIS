from django.db import models

# Create your models here.

class card(models.Model):
    card = models.CharField(max_length=4)
    Card_Number = models.IntegerField()
    PIN = models.IntegerField()
    CVV = models.IntegerField()
    Balance = models.IntegerField()
    Month = models.IntegerField()
    Year = models.IntegerField()
    Name = models.CharField(max_length=250)
    Address = models.CharField(max_length=500)
    Country = models.CharField(max_length=500)
