# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the
#   desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create,
#   modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field
# names.
from django.db import models


class Cities(models.Model):
    city_name = models.CharField(primary_key=True, max_length=50)
    country = models.ForeignKey('Countries', models.DO_NOTHING,
                                db_column='country')

    class Meta:
        managed = False
        db_table = 'cities'


class Countries(models.Model):
    country_name = models.CharField(primary_key=True, max_length=120)

    class Meta:
        managed = False
        db_table = 'countries'


class Dishes(models.Model):
    dish_name = models.CharField(primary_key=True, max_length=50)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dishes'


class Menu(models.Model):
    menu_name = models.CharField(primary_key=True, max_length=50)
    season = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'menu'


class MenuDishes(models.Model):
    dish_name = models.ForeignKey(Dishes, models.DO_NOTHING,
                                  db_column='dish_name')
    menu_name = models.OneToOneField(Menu, models.DO_NOTHING,
                                     db_column='menu_name', primary_key=True)

    class Meta:
        managed = False
        db_table = 'menu_dishes'
        unique_together = (('menu_name', 'dish_name'),)


class Restaurants(models.Model):
    restaurant_name = models.CharField(primary_key=True, max_length=50)
    location = models.ForeignKey(Cities, models.DO_NOTHING,
                                 db_column='location', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurants'


class Staff(models.Model):
    first_name = models.CharField(primary_key=True, max_length=50)
    last_name = models.CharField(max_length=50)
    employer = models.ForeignKey(Restaurants, models.DO_NOTHING,
                                 db_column='employer')
    hire_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'
        unique_together = (('first_name', 'last_name'),)
