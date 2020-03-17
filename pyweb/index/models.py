from django.db import models

# Create your models here.

class Index(models.Model):
    Card = models.CharField(max_length=4, default='Visa')
    Card_number = models.IntegerField(default=1234567891234567)
    PIN = models.IntegerField(default=1234)
    CVV = models.IntegerField(default=123)
    Balance = models.IntegerField(default=0)
    Month = models.IntegerField(default=1)
    Year = models.IntegerField(default=2020)
    Name = models.CharField(max_length=255, default='John')
    Address = models.CharField(max_length=500, default='Street')
    Country = models.CharField(max_length=500, default='Usa')
