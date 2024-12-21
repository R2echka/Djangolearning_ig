from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "catalog/index.html", {'products': products})

def contacts(request):
    return render(request, "catalog/contacts.html")

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product.html', context)