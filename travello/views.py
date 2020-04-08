from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    """dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = '700'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'First Briyani, Then Sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.price = '650'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Bangalore'
    dest3.desc = 'The electronic city'
    dest3.img = 'destination_3.jpg'
    dest3.price = '750'
    dest3.offer = False

    dests = [dest1, dest2, dest3]"""
    
    dests = Destination.objects.all() #connect database and retrieve the value

    return render(request,'index.html',{'dests' : dests})

def destinationMumbai(request):
    dests = Destination.objects.filter(name='Mumbai').all()
    
    return render(request,'mumbai.html',{'dests' : dests})

def destinationChennai(request):
    dests = Destination.objects.filter(name='Chennai').all()

    return render(request,'chennai.html',{'dests' : dests})

def destinationBangalore(request):
    dests = Destination.objects.filter(name='Bangalore').all()
    
    return render(request,'bangalore.html',{'dests' : dests})

def destinationHyderabad(request):
    dests = Destination.objects.filter(name='Hyderabad').all()
    
    return render(request,'hyderabad.html',{'dests' : dests})

def destinationPune(request):
    dests = Destination.objects.filter(name='Pune').all()
    
    return render(request,'pune.html',{'dests' : dests})