from django.shortcuts import render
from rental_car.models import Car, Record, Discount, Rental, PickUpStore, DropOffStore, Store, Client

def home(request):

    car = Car.objects.all()
    record = Record.objects.all()
    discount = Discount.objects.all()
    rental = Rental.objects.all()
    pickUpStore = PickUpStore.objects.all()
    dropOffStore = DropOffStore.objects.all()
    store = Store.objects.all()
    client = Client.objects.all()

    arguments = {'car': car, 'record': record, 'discount': discount, 'rental': rental,
                 'pickUpStore': pickUpStore, 'dropOffStore': dropOffStore, 'store': store, 'client': client }

    return render(request, 'home.html', arguments)


def customerMainPage(request):
    return render(request, 'customerMainPage.html')


def customerSignInForm(request):
    return render(request, 'customerSignInForm.html')


def signupForm(request):
    return render(request, 'signupForm.html')


def staffLoginForm(request):
    return render(request, 'staffLoginForm.html')


def resultPage(request):
    return render(request, 'resultPage.html')


def confirmPage(request):
    return render(request, 'confirmPage.html')


def paymentPage(request):
    return render(request, 'paymentPage.html')


def paymentSuccessPage(request):
    return render(request, 'paymentSuccessPage.html')


def staffMainPage(request):
    return render(request, 'staffMainPage.html')


def staffSearchResultPage(request):
    return render(request, 'staffSearchResultPage.html')


def paymentForm(request):
    return render(request, 'paymentForm.html')
