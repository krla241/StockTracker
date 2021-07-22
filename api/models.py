from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=36)
    price = models.DecimalField(max_digits=19, decimal_places=5)
    noshares = models.IntegerField()
