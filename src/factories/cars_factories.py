import factory
from datetime import date

from src.apps.cars import models
from . import dealer_factories


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Color

    name = 'Red'


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand

    name = 'Audi'


class ModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Model

    brand_id = factory.SubFactory(BrandFactory)
    name = 'a6'


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Car

    color_id = factory.SubFactory(ColorFactory)
    dealer_id = factory.SubFactory(dealer_factories.DealerFactory)
    model_id = factory.SubFactory(ModelFactory)
    engine_type = 'V Engine'
    population_type = 'u'
    price = 31234.0
    fuel_type = 'g'
    status = 'n'
    doors = 2
    capacity = 2
    gear_case = 'a'
    number = 'BC1123AA'
    slug = 'Blah'
    sitting_place = 4
    first_registration_date = date(2020, 10, 9)
    engine_power = 410.5


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Property

    category = 'Decor'
    name = 'Lamp'


class CarPropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CarProperty

    property_id = factory.SubFactory(PropertyFactory)
    car_id = factory.SubFactory(CarFactory)


class PictureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Picture

    car_id = factory.SubFactory(CarFactory)
    url = 'Null'
    position = 'Front'
    metadata = 'Front Photo'


class Order(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Order

    car_id = factory.SubFactory(CarFactory)
    status = 'o'
    first_name = 'Name'
    last_name = 'Surname'
    email = '1221@gmail.com'
    phone = '380993282686'
    message = 'Message text'
