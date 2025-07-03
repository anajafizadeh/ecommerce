from django import forms 
from . import models

class PostProduct(forms.ModelForm):
    class Meta:
        model = models.Products
        fields = ["name", "slug", "description", "price", "image"]