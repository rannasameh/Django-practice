
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include("home.urls")),
    path('contactus/',include("contactus.urls")),
    path('aboutus/',include("aboutus.urls")),
    path('products/',include("products.urls")),


]
