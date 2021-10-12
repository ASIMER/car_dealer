from django.contrib import admin

from .models import Brand, Car, CarProperty, Color, Model, Order, Picture, \
    Property

# Register your models here.
admin.site.register(Car)
admin.site.register(CarProperty)
admin.site.register(Color)
admin.site.register(Picture)
admin.site.register(Order)
admin.site.register(Model)
admin.site.register(Brand)
admin.site.register(Property)
