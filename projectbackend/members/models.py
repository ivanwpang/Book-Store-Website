from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, null = True, blank=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null = True, blank=True, upload_to="images/profile", )

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')