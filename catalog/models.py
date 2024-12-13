from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание')
    img = models.ImageField('Изображение', upload_to='catalog/photo', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField('Цена за покупку')
    created_at = models.DateField('Дата создания')
    updated_at = models.DateField('Дата последнего изменения')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
