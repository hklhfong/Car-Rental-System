"""Carrentsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('    '  , views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('    ', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from Carrentsystem import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from rental_car import views as rental_car
from signup import views as signup
from CarApp import  views as carapp
from django.views.generic import  ListView,DetailView
from CarApp.models import Car

urlpatterns = [
    re_path(r'^$', carapp.home, name='home'),
    re_path(r'^customerSignInForm/$', carapp.customerSignInForm, name='customerSignInForm'),
    re_path(r'^signupForm/$', carapp.signupForm, name='signupForm'),
    re_path(r'^staffLoginForm/$', carapp.staffLoginForm, name='staffLoginForm'),
    re_path(r'^resultPage/$', carapp.resultPage, name='resultPage'),
    re_path(r'^confirmPage/$', carapp.confirmPage, name='confirmPage'),
    re_path(r'^paymentPage/$', carapp.paymentPage, name='paymentPage'),
    re_path(r'^paymentSuccessPage/$', carapp.paymentSuccessPage, name='paymentSuccessPage'),
    re_path(r'^staffMainPage/$', carapp.staffMainPage, name='staffMainPage'),
    re_path(r'^staffSearchResultPage/$', carapp.staffSearchResultPage, name='staffSearchResultPage'),
    re_path(r'^paymentForm/$', carapp.paymentForm, name='paymentForm'),
    re_path(r'^test/$', carapp.test, name='test'),
    re_path(r'^customerMainPage/$', carapp.customerMainPage, name='searchRental'),
    re_path(r'^customerMainPage/search/$', carapp.search, name='searchRental'),
    re_path(r'^customerMainPage/getname/$', carapp.get_name, name='get_name'),
    re_path(r'^detail/$', ListView.as_view(queryset=Car.objects.all().order_by("car_id"),template_name= "contents/detail.html")),
    re_path(r'^customerMainPage/(?P<pk>\d+)$',DetailView.as_view(model=Car,template_name='contents/carinfo.html')),



    path('admin/', admin.site.urls),

    path('index/', rental_car.index),
    path('post1/', rental_car.post1),
    re_path(r'delete/(\d+)/$', rental_car.delete),
    re_path(r'edit/(\d+)/$', rental_car.edit),
    re_path(r'edit/(\d+)/(\w+)$',rental_car.edit),

    path('customer_sign_in/', signup.customer_sign_in),
    path('customer_sign_up/', signup.signup),
    path('staff_sign_in/', signup.staff_sign_in),
    path('staff_main_page/', signup.staff_main_page),
    path('signout/', signup.signout),
    path('staff_signout/', signup.staff_signout),
    path('home/', signup.home),
]

