from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductView.as_view()),
    path("contacts", views.ContactView.as_view()),
    path('<int:pk>', views.ProductDetail.as_view(), name='product')
]