from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("<h1>HELLO WORLD</h1>")
    name = input("Enter a name")
    return render(request,'home.html',{'name':name})

def add(request):

    val1 = int(request.POST['num1'])  # should be in single quote 
    val2 = int(request.POST['num2'])

    res = val1 + val2 
    return render(request,'result.html',{'result':res})