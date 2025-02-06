from .models import Category, Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache

def get_products_by_category(cat):
    products = Product.objects.filter(category_id=Category.objects.get(name=cat).pk)
    return products

def get_cached_products():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'products'
    products = cache.get('products')
    if products:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products