from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm 
from members.models import Profile


class ProfilePageForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = ['bio', 'profile_pic']
        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            #'profile_pic': forms.ImageField(attrs={'class': 'form-control'}),

        }


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    password = None
    username = forms.CharField(max_length=101, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]
       

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=101, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=101, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=101, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2',]
        


