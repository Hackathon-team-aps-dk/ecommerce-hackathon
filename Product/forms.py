from django import forms
from . models import Product

class CreateNewProduct(forms.ModelForm):
    productName = forms.CharField(max_length = 100 , label = "Product Name")
    productDescription = forms.CharField(max_length = 550 , label='Description')
    productCost = forms.IntegerField(label='Cost in ₹')

    class Meta:
        model = Product
        fields = ['productName','productDescription','productCost']