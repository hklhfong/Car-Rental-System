from CarApp.models import Car, Record, Discount, Rental, PickUpStore, DropOffStore, Store, Client
import django_filters

class CarFilter(django_filters.FilterSet):
    number__range = django_filters.NumberFilter()
    number__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    number__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    release_year = django_filters.NumberFilter(field_name='release_date', lookup_expr='year')
    release_year__gt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__gt')
    release_year__lt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__lt')

    class Meta:
        model = Car
        fields = {'type',
                  'car_id',
                  'brand_name',
                  'transmission','price','luggage_size','seat_number','release_year' ,
    }