from django import forms
from home.models import CartDetails

count=[(1,1),(2,2),(3,3),(4,4),(5,5)]

class AddToCartForm(forms.Form):
    quantity=forms.IntegerField(label='Quantity',widget=forms.Select(choices=count),required=True)
