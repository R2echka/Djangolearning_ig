from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductView.as_view()),
    path("contacts/", views.ContactView.as_view()),
    path('<int:pk>', views.ProductDetail.as_view(), name='product'),
    path('create', views.ProductCreate.as_view(), name='create_product'),
    path('<int:pk>/update', views.ProductUpdate.as_view(), name='update_product'),
    path('<int:pk>/delete', views.ProductDelete.as_view(), name='delete_product'),
    ]