from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import ShippingForm
from django.http import HttpResponseRedirect


def home(request):
  return render(request, 'Home.html')

def about(request):
  return render(request, 'AboutUs.html')

def events(request):
  return render(request, 'EventList.html')

def checkout(request):
  return render(request, 'checkout.html')

def shipping(request):
  submitted = False
  if request.method == "POST":
    form = ShippingForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/shipping?submitted = True')
  else:
    form = ShippingForm
    if 'submitted' in request.GET:
      submitted = True
  return render(request, 'Shipping.html', {'form':form, 'submitted':submitted})

def harrypotter(request):
  return render(request, 'HarryPotter.html')


def lordofrings(request):
  return render(request, 'LordRings.html')

def scottpilgrim(request):
  return render(request, 'ScottPilgrim.html')





