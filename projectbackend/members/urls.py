
from django.urls import path
from . import views
from .views import UserEditView, PasswordsChangeView, EditProfilePageView, CreateProfilePageView, DiscussionView, BlogView, CreateDiscussion,UpdatePost
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('editprofile', views.UserEditView.as_view(), name='editprofile'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('password', PasswordsChangeView.as_view(template_name='changepass.html'), name='password'),
    path('pass_success', views.pass_success, name='passsuccess'),
    path('<int:pk>/editbio', EditProfilePageView.as_view(), name='editbio'),
    path('setup_profile', CreateProfilePageView.as_view(), name='setup_profile'),
    path('discussionblog/', DiscussionView.as_view(), name='blog'),
    path('blogview/<int:pk>', BlogView.as_view(), name='blogview'),
    path('addblog', CreateDiscussion.as_view(), name='addpost'),
    path('blogview/edit/<int:pk>', UpdatePost.as_view(), name='editpost'),

]



