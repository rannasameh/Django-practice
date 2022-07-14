"""amazon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from products.views import index_Categories,index_category_products


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include("home.urls")),
    path('contactus/',include("contactus.urls")),
    path('aboutus/',include("aboutus.urls")),
    path('products/',include("products.urls")),
   # path('categories', index_Categories, name='index_categories'),
  #  path('categoryproducts/<category>',index_category_products,name="index_category_products")

]
