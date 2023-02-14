from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home (requests):
    return render(requests, 'itreporting home.html')

def home (requests):
    return render(requests, 'itreporting about.html')

def home (requests):
    return render(requests, 'itreporting contact.html')

