from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Hostel(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    boys = models.BooleanField(default=False, null=True, blank=True)
    girls = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    baths = models.IntegerField()
    beds = models.IntegerField()
    address = models.CharField(max_length=200, null=True)
    area = models.IntegerField()

    def __str__(self):
        return self.name
    
class Flat(models.Model):
    title = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    boys = models.BooleanField(default=False, null=True, blank=True)
    girls = models.BooleanField(default=False, null=True, blank=True)
    email = models.CharField(max_length=200, null=True)
    baths = models.IntegerField()
    beds = models.IntegerField()
    people = models.IntegerField()
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    area = models.IntegerField()

    def __str__(self):
        return self.title
