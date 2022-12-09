from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('covebooks.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
        
]