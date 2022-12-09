from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('checkout/', views.checkout, name='checkout'),
    path('shipping/', views.shipping, name='shipping'),
    path('harrypotter/', views.harrypotter, name='harrypotter'),
    path('lordoftherings/', views.lordofrings, name='lordofrings'),
    path('scottpilgrim/', views.scottpilgrim, name='scottpilgrim'),
]