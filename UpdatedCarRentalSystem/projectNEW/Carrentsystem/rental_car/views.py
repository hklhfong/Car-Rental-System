from django.shortcuts import render
from rental_car.models import Car, Record, Discount, Rental, PickUpStore, DropOffStore, Store, Client

def get(self, request):
    car = Car.objects.all()
    record = Record.objects.all()
    discount = Discount.objects.all()
    rental = Rental.objects.all()
    pickUpStore = PickUpStore.objects.all()
    dropOffStore = DropOffStore.objects.all()
    store = Store.objects.all()
    client = Client.objects.all()