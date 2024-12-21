from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "views")
    search_fields = ("title",)