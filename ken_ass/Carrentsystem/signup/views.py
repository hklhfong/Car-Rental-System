from django.shortcuts import render, redirect
from .forms import CustomerSignInForm, StaffSignInForm, CustomerSignUpForm
from . import models
# Create your views here.

def customer_sign_in(request):
    if request.session.get('signed_in', None):
        return redirect("/home/")
    if request.method == "POST":
        sign_in = CustomerSignInForm(request.POST)
        if sign_in.is_valid():
            customer_username = sign_in.cleaned_data['username']
            customer_password = sign_in.cleaned_data['password']
            try:
                customer = models.Customer.objects.get(username=customer_username)
                if customer.password == customer_password:
                    request.session['signed_in'] = True
                    request.session['username'] = customer.username
                    return redirect('/home/')
                else:
                    notification = "Invalid username or password. Please try again"
            except:
                notification = "Invalid username or password. Please try again"
            return render(request, 'contents/customer_sign_in.html', locals())

    sign_in = CustomerSignInForm()
    return render(request, 'contents/customer_sign_in.html', locals())

def staff_sign_in(request):
    if request.session.get('staff_signed_in', None):
        return redirect("/home/")
    if request.method == "POST":
        sign_in_staff = StaffSignInForm(request.POST)
        if sign_in_staff.is_valid():
            staff_number = sign_in_staff.cleaned_data['staff_number']
            staff_password = sign_in_staff.cleaned_data['password']
            try:
                staff = models.Staff.objects.get(staff_number=staff_number)
                if staff.password == staff_password:
                    request.session['staff_signed_in'] = True
                    request.session['staff_number'] = staff.staff_number
                    request.session['first_name'] = staff.first_name
                    request.session['last_name'] = staff.last_name
                    return redirect('/staff_main_page/')
                else:
                    notification = "Invalid staff number or password. Please try again"
            except:
                notification = "Invalid username or password. Please try again"
            return render(request, 'contents/staff_sign_in.html', locals())

    sign_in_staff = StaffSignInForm()
    return render(request, 'contents/staff_sign_in.html', locals())

def signup(request):
    if request.session.get('signed_in', None):

        return redirect("/home/")

    if request.method == "POST":

        sign_up = CustomerSignUpForm(request.POST)

        if sign_up.is_valid():
            customer_first_name = sign_up.cleaned_data['first_name']
            customer_last_name = sign_up.cleaned_data['last_name']
            customer_username = sign_up.cleaned_data['username']
            customer_password = sign_up.cleaned_data['password']
            customer_repeat_password = sign_up.cleaned_data['repeat_password']
            email_address = sign_up.cleaned_data['email_address']
            gender = sign_up.cleaned_data['gender']

            if customer_repeat_password != customer_password:

                notification = "The password and the confirm password do not match"
                return render(request, 'contents/customer_sign_up.html', locals())

            email_used = models.Customer.objects.filter(email_address=email_address)
            if email_used:

                notification = "The email address has been used"
                return render(request, 'contents/customer_sign_up.html', locals())

            username_used = models.Customer.objects.filter(username=customer_username)
            if username_used:

                notification = "The username has been used"
                return render(request, 'contents/customer_sign_up.html', locals())

            new_customer_account = models.Customer.objects.create()
            new_customer_account.first_name = customer_first_name
            new_customer_account.last_name = customer_last_name
            new_customer_account.username = customer_username
            new_customer_account.email_address = email_address
            new_customer_account.password = customer_password
            new_customer_account.gender = gender
            new_customer_account.save()
            return redirect('/customer_sign_in/')

    sign_up = CustomerSignUpForm()
    return render(request, 'contents/customer_sign_up.html', locals())

def home(request):
    pass
    return render(request, 'contents/home.html')


def staff_main_page(request):
    pass
    return render(request, 'contents/staff_main_page.html')

def signout(request):
    if not request.session.get('signed_in', None):
        return redirect('/home/')
    request.session.flush()
    return redirect('/home/')

def staff_signout(request):
    if not request.session.get('staff_signed_in', None):
        return redirect('/home/')
    request.session.flush()
    return redirect('/home/')



