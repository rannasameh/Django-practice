from django.contrib import admin
from django.urls import path
from aboutus.views import aboutus


urlpatterns = [
    path('',aboutus,name="aboutus"),
]