from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('Home Page')

def product(request):
    return HttpResponse('Product')

def customers(request):
    return HttpResponse('Customers')