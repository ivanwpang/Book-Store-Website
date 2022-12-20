from django.shortcuts import render
from django.template import loader
from members.models import Product





def home(request):
  return render(request, 'Home.html')

def about(request):
  return render(request, 'AboutUs.html')

def events(request):
  return render(request, 'EventList.html')

def checkout(request):
  return render(request, 'checkout.html')

def shipping(request):
  return render(request, 'Shipping.html')

def harrypotter(request):
  return render(request, 'HarryPotter.html')


def lordofrings(request):
  return render(request, 'LordRings.html')

def scottpilgrim(request):
  return render(request, 'ScottPilgrim.html')









    




