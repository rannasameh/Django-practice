from django.shortcuts import render
from products.forms import ProductModelForm
from products.models import Products, Category
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponse
import os
# Create your views here.
class CreateProductView(CreateView):
    form_class = ProductModelForm
    template_name = "products/create.html"
    success_url = "/products"


class EditProductView(UpdateView):
    model = Products
    form_class = ProductModelForm
    template_name = "products/edit.html"


class ProductDetailView(DetailView):
    template_name = "products/product.html"
    model = Products


class ProductslistView(ListView):
    template_name = "products/productspage.html"
    model = Products
    context_object_name = "products"


class CategorylistView(ListView):
    template_name = "products/categories.html"
    model = Category
    context_object_name = "categories"


class DeleteProductView(DeleteView):
    model = Products
    success_url = "/products"


class CreateProfileView(View):
    def get(self, request):
        form = ProductModelForm()
        return render(request, "products/create.html", context={
            "form": form
        })

    def post(self, request):
        form = ProductModelForm(request.POST, request.FILES)
        form.save()
        return HttpResponse(request.FILES)




