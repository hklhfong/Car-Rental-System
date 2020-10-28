from django.db import models


class SearchList(models.Model):
    pick_up_city = models.CharField(label='Pickup City', max_length=100)
    drop_off_city = models.CharField(label='Dropoff City', max_length=100)
    pick_up_date = models.DateField(label='Pickup date')
    drop_off_date = models.DateField(label='Dropoff date')

    def __str__(self):
        return self.name