from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction_list(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    current_price = models.IntegerField()
    image_url = models.CharField(max_length=350, default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=64)
    


class Bids(models.Model):
    pass


class Comments(models.Model):
    pass