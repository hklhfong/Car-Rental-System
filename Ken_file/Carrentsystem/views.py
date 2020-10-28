
from CarApp.models import Car, Record, Discount, Rental, PickUpStore, DropOffStore, Store, Client
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render,redirect



def home(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {'cars': cars})


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

def test(request):
    clients = Client.objects.all()
    return render(request, 'chart.html', {'clients': clients})

from Carrentsystem.filter import  CarFilter

def search(request):
    Car_list = Car.objects.all().order_by('type')
    Car_filter = CarFilter(request.GET, queryset=Car_list)
    return render(request, 'customerMainPagenew.html', {'filter': Car_filter})
