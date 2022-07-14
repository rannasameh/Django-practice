from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=100, default="watch.jpg")

    def __str__(self):
        return f"{self.name}"


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Products(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    price = models.FloatField()
    instock = models.IntegerField()
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img = models.FileField(upload_to="products/static/images")
    countries = models.ManyToManyField(Country, null=True)

    def __str__(self):
        return f"{self.name}"

    def get_delete_url(self):
        return reverse("delete_product", args=[self.id])

    def get_updated_url(self):
        return reverse("edit_product", args=[self.id])

    def get_absolute_url(self):
        return reverse("itemproductpage", args=[self.id])
