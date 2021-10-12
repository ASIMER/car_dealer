from django.db import models


# Create your models here.


class Car(models.Model):
    FUEL_TYPE_CHOICES = [
            ('p', 'Petrol'),
            ('gas', 'Gas'),
            ('dis', 'Diesel'),
            ('el', 'Electric'),
            ('hg', 'Hydrogen'),
            ]
    GEAR_CASE_CHOICES = [
            ('m', 'Mechanic'),
            ('a', 'Automatic'),
            ]

    STATUS_CHOICES = [
            ('sol', 'sold'),
            ('sel', 'selling'),
            ('arc', 'archived'),
            ]

    SEATS_CHOICES = [
            ('2', 'two'),
            ('3', 'three'),
            ('4', 'four'),
            ('5', 'five'),
            ('more', 'more then five')
            ]
    model = models.ForeignKey('Model', on_delete=models.CASCADE, null=True)
    color = models.ForeignKey('Color', on_delete=models.CASCADE, null=True)
    dealer = models.ForeignKey('dealers.Dealer', on_delete=models.CASCADE,
                               null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    engine_power = models.IntegerField()
    gear_case = models.CharField(max_length=1, choices=GEAR_CASE_CHOICES)
    fuel_type = models.CharField(max_length=3, choices=FUEL_TYPE_CHOICES)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    engine_type = models.CharField(max_length=50)
    population_type = models.CharField(max_length=50)
    doors = models.IntegerField()
    number = models.CharField(max_length=10)
    sitting_place = models.CharField(max_length=4, choices=SEATS_CHOICES)
    first_registration_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.dealer} selling a(an) {self.model}'


class Color(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=15, unique=True)
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Picture(models.Model):
    picture = models.IntegerField(primary_key=True)
    position = models.IntegerField()
    metadata = models.CharField(max_length=30)
    url = models.ImageField(verbose_name="Car photo", null=True, blank=True)
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'metadata of picture is {self.metadata}'


class Property(models.Model):
    category = models.CharField(max_length=10)
    name = models.CharField(max_length=15)

    def __str__(self):
        return f'Category {self.category} with name {self.name}'


class CarProperty(models.Model):
    car_property = models.IntegerField(primary_key=True)
    property = models.ForeignKey(to=Property, on_delete=models.CASCADE,
                                 null=True)
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE)


class Order(models.Model):
    STATUS_CHOICES = [
            ('sol', 'sold'),
            ('sel', 'selling'),
            ('arc', 'archived'),
            ]

    order = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=244)
    phone_number = models.CharField(max_length=10)
    message = models.TextField(max_length=500)
    car = models.ForeignKey(to=Car, on_delete=models.SET('Sold'))
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return f'The buyer {self.first_name} {self.last_name} want to buy car {self.car} with status {self.status}'
