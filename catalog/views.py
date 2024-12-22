from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import DetailView, ListView, View

# Create your views here.

class ProductView(ListView):
    model= Product
    template_name = "catalog/index.html"
    context_object_name = 'products'

class ContactView(ListView):
    model= Product
    template_name= "catalog/contacts.html"

class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'