
from django.urls import path

from contactus.views import contactuspage


urlpatterns = [
    path('', contactuspage,name="contactus"),
]
