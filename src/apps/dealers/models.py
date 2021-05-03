from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    code = models.IntegerField(unique=True, null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE,
                                   null=True)

    def __str__(self):
        return f'{self.country_id.name} | {self.name}'


class Dealer(AbstractUser):
    title = models.CharField(max_length=50)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
