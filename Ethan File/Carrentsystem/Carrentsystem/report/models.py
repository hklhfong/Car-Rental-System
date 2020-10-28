from django.db import models

# Create your models here.
class Report(models.Model):

    car_id = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=30)
    transmission = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    luggage_size = models.CharField(max_length=10)
    seat_number = models.CharField(max_length=10)
    release_year = models.CharField(max_length=10)
    total_rent_january = models.CharField(max_length=4)
    total_rent_february = models.CharField(max_length=4)
    total_rent_march = models.CharField(max_length=4)
    total_rent_april= models.CharField(max_length=4)
    total_rent_may = models.CharField(max_length=4)
    total_rent_june = models.CharField(max_length=4)
    total_rent_july = models.CharField(max_length=4)
    total_rent_august = models.CharField(max_length=4)
    total_rent_september = models.CharField(max_length=4)
    total_rent_october = models.CharField(max_length=4)
    total_rent_november = models.CharField(max_length=4)
    total_rent_december = models.CharField(max_length=4)

    class Meta:
        db_table = "report"

    def __str__(self):
        return self.name