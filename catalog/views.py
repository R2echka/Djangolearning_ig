from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.views.generic import DetailView, ListView, View, CreateView, UpdateView, DeleteView

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

class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = ''

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = ''

class ProductDelete(DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = ''