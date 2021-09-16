from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length = 100)
    productDescription = models.CharField(max_length = 550)
    productCost = models.IntegerField()
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , null =True)

    def __str__(self):
        return self.productName 