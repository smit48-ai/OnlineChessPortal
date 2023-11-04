from django.contrib import admin
from django.urls import path,include
from .views import user_login,user_signup,user_profile,user_logout,uploadProfile,verify_email

urlpatterns = [
   path("login/",user_login,name='login'),
   path("signup/",user_signup,name='signup'),
   path("logout/",user_logout,name='logout'),
   path("<int:pk>/",user_profile, name='index'),
   path('verify/<str:token>/', verify_email, name='verify_email'),
   path("UpdateProfile/",uploadProfile, name='profile')
]
