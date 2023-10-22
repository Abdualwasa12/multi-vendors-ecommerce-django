from django import forms
from shop.models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['category', 'thumbnail', 'name', 'description', 'price','phone',]


