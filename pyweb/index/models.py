from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=250)
    kartica_usera=models.ManyToManyField(User, through='Verifikacija')


class Kartica(models.Model):
    Card_number = models.CharField(max_length=19,default='1234 5678 9123 4567',primary_key=True)
    CVV = models.CharField(max_length=3,default='123')
    Balance = models.IntegerField(default=0)
    korisnik=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Card_number


class Verifikacija(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    kartica=models.ForeignKey(Kartica, on_delete=models.CASCADE)
    pin=models.CharField(max_length=4)
