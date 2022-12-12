from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import ShippingForm
from django.http import HttpResponseRedirect
from members.models import Profile
from .models import * 


def home(request):
  return render(request, 'Home.html')

def payment(request):
  return render(request, 'payment.html')

def about(request):
  return render(request, 'AboutUs.html')

def events(request):
  return render(request, 'EventList.html')

def checkout(request):

  if request.user.is_authenticated:
      customer = request.user.customer
      order, created = Order.objects.get_or_create(customer=customer, complete=False)
      items = order.orderitem_set.all()
  else:
    items = [ ]
  
  context = {'items':items}
  return render(request, 'checkout.html', context)

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









    




