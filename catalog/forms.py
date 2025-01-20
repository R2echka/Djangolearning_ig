from django import forms
from django.core.exceptions import ValidationError
from .models import Product

forbidden = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'img', 'category', 'price', 'created_at']
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название продукта'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Добавьте описание'})
        self.fields['img'].widget.attrs.update({'class': 'form-control', 'placeholder': 'И картинку'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'К какой категории относится продукт'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Куда же продукт без цены'})
        self.fields['created_at'].widget.attrs.update({'class': 'form-control', 'placeholder': 'А ещё укажите сегодняшнюю дату'})


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if int(price) < 0:
            raise ValidationError("Пожалуйста, введите неотрицательное значение цены.")
    
    def clean(self):
        super().clean()
        name = self.cleaned_data.get('name')
        desc = self.cleaned_data.get('description')
        if name and desc and (any(word in name.lower() for word in forbidden) or any(word in desc.lower() for word in forbidden)):
            raise ValidationError('Пожалуйста, не используйте запрещённые слова.')