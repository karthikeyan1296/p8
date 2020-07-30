from django.shortcuts import render
from django.http import HttpResponse
from math import factorial
# Create your views here.

def index(request):
    return HttpResponse("<h1>welcome to views of an app</h1>")

def home(request):
    return render(request,"rsk2/home.html",{'name':"karthi"})

def fact(request,n):
    n=int(n)
    return HttpResponse("<h3>factorial is {}</h3>".format(factorial(n)))

def child(request):
    return render(request,"child.html")

def base(request):
    return render(request,"rsk2/base.html")