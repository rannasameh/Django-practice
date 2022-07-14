from django.urls import path,include
from products.views import ProductDetailView,CreateProductView,DeleteProductView,EditProductView,ProductslistView
from products.views import CreateProfileView

urlpatterns = [
    path('',ProductslistView.as_view(),name="index_products"),
    path("newprofile", CreateProfileView.as_view(), name ="createprofile"),
    path('create/', CreateProductView.as_view(), name="create_product"),
    path('<int:pk>/',ProductDetailView.as_view(),name="itemproductpage"),
    path('delete/<int:pk>/',DeleteProductView.as_view(),name="delete_product"),
    path('edit/<int:pk>/',EditProductView.as_view(),name="edit_product"),
]