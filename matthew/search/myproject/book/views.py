from django.http import HttpResponse
from django.shortcuts import render_to_response 
from .models import MYBOOK

def index(request):
    return render_to_response('index.html')

def insert(request):
    NAME = request.GET['name']
    PRICE = float(request.GET['price'])
    MYBOOK.objects.create(name=NAME, price=PRICE)
    return render_to_response('index.html', {'name':NAME, 'price': PRICE})

def query(request):
    query = request.GET['book']
    books = MYBOOK.objects.filter(name__icontains = query)
    return render_to_response('search.html', {'query':query, 'books': books})
