from django.http import HttpResponse
from django.shortcuts import render
from store.models import Collection
import json

# Create your views here.
# Views are functions that handle requests and return responses. Similar to controllers in Express
# or services in NestJS

def calculate():
    x = 1
    y = 1
    return x

def say_hello(request):
    collections = Collection.objects.get(id=1)
    print(collections.__dict__)
    # return collections
    return HttpResponse('Hello World!')

def say_hello_html(request):
    x = calculate()
    return render(request, 'hello.html', { 'name': 'Simon' })