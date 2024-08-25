from django.db import models

# Create your models here.
from shopify_auth.models import AbstractShopUser


class AuthAppShopUser(AbstractShopUser):
    pass


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
