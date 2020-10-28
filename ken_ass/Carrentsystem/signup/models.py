from django.db import models

# Create your models here.

GENDER = (
    ('male', 'male'),
    ('female', 'female'),
)

class Customer(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "Customer"

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    staff_number = models.IntegerField()
    password = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_number

    class Meta:
        db_table = "Staff"