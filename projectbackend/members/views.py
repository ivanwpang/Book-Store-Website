
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.views import generic
from django.urls import reverse_lazy
from .forms import EditProfileForm, PasswordChangingForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from members.models import Profile
from django.views.generic import TemplateView, ListView, CreateView




            

def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "Username or Password Incorrect")
            return redirect('login')
    
    else:
        return render(request, 'login.html', {})


def register(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Signup Succesfull")
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'Signup.html', {
        'form':form,
    })


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('home')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'editprofile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

def myprofile(request):
  return render(request, 'myprofile.html')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    #messages.success(request, "Password Successfully changed!")
    success_url = reverse_lazy('passsuccess')

def pass_success(request):
    return render(request, 'passsuccess.html', {})
    

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'editbio.html'
    fields = ['bio', 'profile_pic']
    success_url = reverse_lazy('home')

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'createprofile.html'
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)