from django.db import models


class MYBOOK(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name+':'+str(self.price)