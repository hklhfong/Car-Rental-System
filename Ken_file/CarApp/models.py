from django.db import models
from django.forms import ModelForm

# Create your models here.
class Car(models.Model):

    BRAND_NAME = (
        ('LAND ROVER', 'LAND ROVER'),
        ('BMW', 'BMW'),
        ('VOLVO', 'VOLVO'),
        ('VOLKSWAGEN', 'VOLKSWAGEN'),
        ('TOYOTA', 'TOYOTA'),
        ('SAAB', 'SAAB'),
        ('RENAULT', 'RENAULT'),
        ('NISSAN', 'NISSAN'),
        ('MITSUBISHI', 'MITSUBISHI'),
        ('MERCEDES-BENZ', 'MERCEDES-BENZ'),
        ('MAZDA', 'MAZDA'),
        ('HONDA', 'HONDA'),
        ('EUNOS', 'EUNOS'),
        ('DATSUN', 'DATSUN'),
        ('CHRYSLER', 'CHRYSLER'),
        ('AUDI', 'AUDI'),
        ('ALFA ROMEO', 'ALFA ROMEO'),
        ('PEUGEOT', 'PEUGEOT'),
        ('NULL', 'NULL'),
    )

    car_id = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=13, choices=BRAND_NAME)
    type = models.CharField(max_length=30)
    transmission = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    luggage_size = models.CharField(max_length=10)
    seat_number = models.CharField(max_length=10)
    release_year = models.CharField(max_length=10)
    record = models.ForeignKey('Record', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "car"

    def __str__(self):
        return self.name


class Record(models.Model):

    record_id = models.IntegerField(primary_key=True)
    accident_type = models.CharField(max_length=30)
    accident_address = models.CharField(max_length=30)
    client = models.ForeignKey('Client', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "Record"

    def __str__(self):
        return self.name

class Discount(models.Model):

    discount_id = models.IntegerField(primary_key=True)
    discount_code = models.IntegerField(null=True)
    starting_date = models.DateField()
    ending_date = models.DateField()

    class Meta:
        db_table = "Discount"

    def __str__(self):
        return self.name

class Rental(models.Model):

    CITY =(
        ('Sydney', 'Sydney'),
        ('Melbourne', 'Melbourne'),
        ('Brisbane', 'Brisbane'),
    )

    rental_id = models.IntegerField(primary_key=True)
    rent_date = models.DateField()
    end_rent_date = models.DateField()
    rent_price_total = models.IntegerField(null=True)
    pick_up_city = models.CharField(max_length=9, choices=CITY)
    drop_off_city = models.CharField(max_length=9, choices=CITY)
    car = models.ForeignKey('Car', blank=True, null=True, on_delete=models.CASCADE)
    client = models.ForeignKey('Client', blank=True, null=True, on_delete=models.CASCADE)
    insurance_number = models.CharField(max_length=20)
    discount = models.ForeignKey('Discount', blank=True, null=True, on_delete=models.CASCADE)
    pick_up_store = models.ForeignKey('PickUpStore', blank=True, null=True, on_delete=models.CASCADE)
    drop_off_store = models.ForeignKey('DropOffStore', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "Rental"

    def __str__(self):
        return self.name

class PickUpStore(models.Model):

    pick_up_store_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey('Store', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "PickUpStore"

    def __str__(self):
        return self.name

class DropOffStore(models.Model):

    drop_off_store_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey('Store', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "DropOffStore"

    def __str__(self):
        return self.name

class Store(models.Model):

    STATE =(
        ('Queensland', 'Queensland'),
        ('South Australia', 'South Australia'),
        ('Tasmania', 'Tasmania'),
        ('Victoria', 'Victoria'),
        ('New South Wales', 'New South Wales'),
    )

    store_id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=30)
    store_address = models.CharField(max_length=30)
    store_phone = models.TextField(default="null")
    store_city = models.CharField(max_length=30)
    store_state_name = models.CharField(max_length=15, choices=STATE)

    class Meta:
        db_table = "Store"

    def __str__(self):
        return self.name

class Client(models.Model):

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    client_id = models.IntegerField(primary_key=True)
    client_name = models.CharField(max_length=30)
    client_phone = models.CharField(max_length=30)
    client_address = models.CharField(max_length=50)
    client_brithday = models.DateField()
    client_occupation = models.CharField(max_length=20)
    client_gender = models.CharField(max_length=1, choices=GENDER)

    class Meta:
        db_table = "Client"

    def __str__(self):
        return self.name

