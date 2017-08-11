from django.db import models
from django.contrib.auth.models import User
import math


# Create your models here.
class Model(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cam_sites = models.ManyToManyField(CamSite, null=True)
    address = models.CharField(max_length=30, blank=True)
    address_2 = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30)


class CamSite(models.Model):
    site_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    link = models.CharField(max_length=400)


class WishList(models.Model):
    model = models.ForeignKey(models)
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True)


class WishListLines(models):
    product = models.ForeignKey(Product)
    wish_list = models.ForeignKey(WishList)
    purchased = models.BooleanField(default=False)


class Product(models.Model):
    cost = models.DecimalField(decimal_places=2, max_length=12)
    price = models.DecimalField(decimal_places=2, max_length=12)
    vendor = models.ForeignKey(Vendor)

    @property
    def suggest_price(self):
        return math.ceil((self.cost * 2) + self.vendor.drop_shipping_price) - 1


class Vendor(models.Model):
    drop_shipping_price = models.DecimalField(decimal_places=2, max_length=6)


class Order(models.Model):
    pass


class Shipment(models.Model):
    pass


class OrderLine(models.Model):
    order = models.ForeignKey(Order)
