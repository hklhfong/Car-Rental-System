from CarApp.models import Car, Client
from django.shortcuts import render
from django.http import HttpResponseRedirect


def home(request):
    cars = Car.objects.all()
    return render(request, 'contents/home.html', {'cars': cars})


def customerMainPage(request):
    return render(request, 'contents/customerMainPage.html')


def customerSignInForm(request):
    return render(request, 'contents/customerSignInForm.html')


def signupForm(request):
    return render(request, 'contents/signupForm.html')


def staffLoginForm(request):
    return render(request, 'contents/staffLoginForm.html')


def resultPage(request):
    return render(request, 'contents/resultPage.html')


def confirmPage(request):
    return render(request, 'contents/confirmPage.html')


def paymentPage(request):
    return render(request, 'contents/paymentPage.html')


def paymentSuccessPage(request):
    return render(request, 'contents/paymentSuccessPage.html')


def staffMainPage(request):
    return render(request, 'contents/staffMainPage.html')


def staffSearchResultPage(request):
    return render(request, 'contents/staffSearchResultPage.html')


def paymentForm(request):
    return render(request, 'contents/paymentForm.html')


def test(request):
    clients = Client.objects.all()
    return render(request, 'contents/chart.html', {'clients': clients})


def mainpage(request):
    return render(request, 'contents/customerMainPage.html')


from CarApp.filter import CarFilter


def search(request):
    Car_list = Car.objects.all().order_by('type')
    Car_filter = CarFilter(request.GET, queryset=Car_list)
    return render(request, 'contents/customerMainPage.html', {'filter': Car_filter})


from .form import NameForm


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request.path_info)
        else:
            form = NameForm()
    return render(request, 'contents/customerMainPage.html', {'form': form})
