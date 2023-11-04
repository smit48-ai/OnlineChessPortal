from django.contrib import admin
from django.urls import path,include
from .views import playView,joinView

urlpatterns = [
    path("play/", playView, name="playView"),
    path("join/", joinView, name="joinView")
]