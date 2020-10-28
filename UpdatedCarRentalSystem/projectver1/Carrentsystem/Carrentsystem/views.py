from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


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
