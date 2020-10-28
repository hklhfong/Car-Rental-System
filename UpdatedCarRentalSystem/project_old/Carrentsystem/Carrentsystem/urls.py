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
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('customerMainPage/', views.customerMainPage, name='customerMainPage'),
    path('customerSignInForm/', views.customerSignInForm, name='customerSignInForm'),
    path('signupForm/', views.signupForm, name='signupForm'),
    path('staffLoginForm/', views.staffLoginForm, name='staffLoginForm'),
    path('resultPage/', views.resultPage, name='resultPage'),
    path('confirmPage/', views.confirmPage, name='confirmPage'),
    path('paymentPage/', views.paymentPage, name='paymentPage'),
    path('paymentSuccessPage/', views.paymentSuccessPage, name='paymentSuccessPage'),
    path('staffMainPage/', views.staffMainPage, name='staffMainPage'),
    path('staffSearchResultPage/', views.staffSearchResultPage, name='staffSearchResultPage'),
    path('paymentForm/', views.paymentForm, name='paymentForm')
]
