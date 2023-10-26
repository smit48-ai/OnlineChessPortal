from django.contrib import admin
from django.urls import path,include
from .views import user_login,user_signup,user_profile

urlpatterns = [
   path("login/",user_login,name='login'),
   path("signup/",user_signup,name='signup'),
   path("<int:pk>/",user_profile, name='index'),
]
