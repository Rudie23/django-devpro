from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<html><body><h3>Hello, world. You're at the polls index.</h3></body></html>")
