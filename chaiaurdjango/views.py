from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("hello world, we are in about page")

def contact(request):
    return HttpResponse("hello world, we are in contact page")

