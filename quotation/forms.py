from django import forms
from .models import Product

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['usage_location', 'prod_category', 'prod_type', 'prod_name', 'desc', 'stock', 'price', 'picture']
