from django.contrib import admin
from django.urls import path, re_path

from rental_car import views as rental_car
from signup import views as signup
from report import views as reportsys

urlpatterns = [
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
    path('report/', reportsys.report)
]