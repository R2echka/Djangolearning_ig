from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Укажите свой email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Придумайте пароль'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Точно запомнили?'})
