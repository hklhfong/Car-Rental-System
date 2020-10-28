from django.db import models

# Create your models here.
class Car(models.Model):

    car_id = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    transmission = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    luggage_size = models.CharField(max_length=10)
    seat_number = models.CharField(max_length=10)
    release_year = models.CharField(max_length=10)
    record_id = models.ForeignKey('Record', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "car"

class Record(models.Model):

    record_id = models.IntegerField(primary_key=True)
    accident_type = models.CharField(max_length=30)
    accident_address = models.CharField(max_length=30)
    client_id = models.ForeignKey('Client', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "Record"

class Discount(models.Model):

    discount_id = models.IntegerField(primary_key=True)
    discount_code = models.IntegerField(null=True)
    starting_date = models.DateField()
    ending_date = models.DateField()

    class Meta:
        db_table = "Discount"

class Rental(models.Model):
    rental_id = models.IntegerField(primary_key=True)
    rent_date = models.DateField()
    end_rent_date = models.DateField()
    rent_price_total = models.IntegerField(null=True)
    pick_up_city = models.CharField(max_length=20)
    drop_off_city = models.CharField(max_length=20)
    car_id = models.ForeignKey('Car', blank=True, null=True, on_delete=models.CASCADE)
    client_id = models.ForeignKey('Client', blank=True, null=True, on_delete=models.CASCADE)
    insurance_number = models.CharField(max_length=20)
    discount_id = models.ForeignKey('Discount', blank=True, null=True, on_delete=models.CASCADE)
    pick_up_store_id = models.ForeignKey('PickUpStore', blank=True, null=True, on_delete=models.CASCADE)
    drop_off_store_id = models.ForeignKey('DropOffStore', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "Rental"

class PickUpStore(models.Model):

    pick_up_store_id = models.IntegerField(primary_key=True)
    store_id = models.ForeignKey('Store', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "PickUpStore"

class DropOffStore(models.Model):

    drop_off_store_id = models.IntegerField(primary_key=True)
    store_id = models.ForeignKey('Store', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "DropOffStore"

class Store(models.Model):

    store_id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=30)
    store_address = models.CharField(max_length=30)
    store_phone = models.TextField(default="null")
    store_city = models.CharField(max_length=30)
    store_state_name = models.CharField(max_length=30)

    class Meta:
        db_table = "Store"

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
