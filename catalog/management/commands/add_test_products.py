from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category, created = Category.objects.get_or_create(name='category1')

        products = [
            {'name': 'something', 'description': 'meow', 'img': '', 'category': category, 'price': 0, 'created_at': '1900-04-15', 'updated_at': '2024-12-04'},
            {'name': 'product', 'description': '', 'img': '', 'category': category, 'price': 290, 'created_at': '2000-10-10', 'updated_at': '2024-12-04'},
        ]

        for product_data in products:
            product_data['category'] = category
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))