from CarApp.models import Car, Record, Discount, Rental, PickUpStore, DropOffStore, Store, Client
import django_filters

class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = {'type': ['icontains'],
                  'car_id': ['exact'],
                  'brand_name': ['icontains'],
                  'transmission': ['exact'],
                  'price': ['exact'],
                  'luggage_size': ['icontains'],
                  'seat_number': ['icontains'],
                  'release_year' : ['exact']
    }