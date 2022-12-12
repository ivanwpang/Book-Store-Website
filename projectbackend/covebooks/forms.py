from django import forms
from django.forms import ModelForm
from .models import Shipping

#Create a Shipping Form
class ShippingForm(ModelForm):
    class Meta:
        model = Shipping
        fields = "__all__"
        labels = {
            'firstname': '',
            'lastname': '',
            'phoneNumber': '',
            'address': '',
            'city': '',
            'state': '',
            'zipCode': '',
            'instructions': '',   
        }
        widgets = {
            'firstname': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'First Name'}),
            'lastname': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Last Name'}),
            'phoneNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Phone Number'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Address'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'City'}),
            'state': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'State'}),
            'zipCode': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Zip Code'}),
            'instructions': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Special Delivery Instructions'}),          
        }
        