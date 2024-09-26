from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
<<<<<<< HEAD
        fields = ['product_name','location_number', 'quantity', 'preview1', 'volume', 'standard', 'special_standard', 'precision', 'is_defective', 'spare1', 'product_image', 'detail_image']
=======
        fields = ['product_name','location_number', 'quantity', 'preview1', 'volume', 'standard', 'special_standard', 'precision', 'is_defective', 'date_received', 'spare1', 'product_image', 'detail_image']
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
