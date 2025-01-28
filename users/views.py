from django.shortcuts import render
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserRegisterForm
from django.views.generic import CreateView
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

# Create your views here.
class UserCreate(CreateView):
    model = CustomUser
    form_class = CustomUserRegisterForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        send_mail(
            subject='Приветствие на сайте',
            message='Поздравляем с успешной регистрацией на сайте',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email,])
        return super().form_valid(form)