from django.contrib import admin
from django.urls import path,include
from .views import CreateContest,Detailsview

urlpatterns = [
    path("create",CreateContest, name="Create"),
    path("<int:pk>", Detailsview, name="Page")
]