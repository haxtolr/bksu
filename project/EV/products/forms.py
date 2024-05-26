from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','location_number', 'quantity', 'preview1', 'volume', 'standard', 'special_standard', 'precision', 'is_defective', 'spare1', 'product_image', 'detail_image']