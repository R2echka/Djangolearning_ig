from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("contacts", views.contacts),
    path('<int:pk>', views.ProductDetail.as_view(), name='product')
]