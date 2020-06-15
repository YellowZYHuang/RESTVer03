from django.db import models


# Create your models here.
class Invoices2020M01(models.Model):
    Date = models.CharField(max_length=8)
    Amount = models.DecimalField(max_digits=10, decimal_places=5)
