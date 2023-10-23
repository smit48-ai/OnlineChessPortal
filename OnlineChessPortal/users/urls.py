from django.contrib import admin
from django.urls import path,include
from .views import user_login,user_signup

urlpatterns = [
   path("login/",user_login,name='login'),
   path("signup/",user_signup,name='signup')
]