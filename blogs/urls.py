from django.urls import path
from . import views
from blogs.views import BlogList, BlogDetail, BlogCreate, BlogUpdate, BlogDelete

app_name = "blogs"

urlpatterns = [
    path('', BlogList.as_view(), name='blog'),
    path('<int:pk>', views.BlogDetail.as_view(), name='post'),
    path('product/create', views.BlogCreate.as_view(), name='create_post'),
    path('product/<int:pk>/update', views.BlogUpdate.as_view(), name='update_post'),
    path('product/<int:pk>/delete', views.BlogDelete.as_view(), name='delete_post'),
]