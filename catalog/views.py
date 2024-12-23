from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView, ListView, View

# Create your views here.

class ProductView(ListView):
    model= Product
    template_name = "catalog/index.html"
    context_object_name = 'products'

class ContactView(View):
    template_name= "catalog/contacts.html"
    def get(self, request):
        return render(request, "catalog/contacts.html")

class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'