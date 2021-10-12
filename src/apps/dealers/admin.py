from django.contrib import admin

from .models import City, Country, Dealer

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Dealer)
