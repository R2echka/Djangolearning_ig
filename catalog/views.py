from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Product, Category
from .forms import ProductForm, ProductModeratorForm
from .services import get_products_by_category, get_cached_products
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, View, CreateView, UpdateView, DeleteView

# Create your views here.

class ProductView(ListView):
    model= Product
    template_name = "catalog/index.html"
    context_object_name = 'products'

    def get_queryset(self):
        return get_cached_products()

class ContactView(LoginRequiredMixin, View):
    template_name= "catalog/contacts.html"
    def get(self, request):
        return render(request, "catalog/contacts.html")

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = '/'

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied

class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = '/'

class ProductsByCategory(LoginRequiredMixin, ListView):
    model= Category
    template_name = "catalog/filtered_products.html"
    context_object_name = 'filtered_products'
    
    def get_queryset(self):
        return get_products_by_category(self.kwargs.get('name'))