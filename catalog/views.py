from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import DetailView

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "catalog/index.html", {'products': products})

def contacts(request):
    return render(request, "catalog/contacts.html")

class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'