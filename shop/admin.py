from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    prepopulated_fields ={'slug': ('name',)}
    
@admin.register(Category)
class Category(admin.ModelAdmin):
    prepopulated_fields ={'slug': ('name',)}
    
admin.site.register(ProductImages)
