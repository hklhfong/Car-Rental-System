from django.http import HttpResponse
from django.shortcuts import render_to_response 
from .models import SearchList

def index(request):
    return render_to_response('index.html')

def query(request):
    query = request.GET['book']
    books = MYBOOK.objects.filter(name__icontains = query)
    return render_to_response('search.html', {'query':query, 'books': books})
