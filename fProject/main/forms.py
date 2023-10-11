from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'category', 'description', 'price', 'stock', 'available', 'slug', 'storage1',
                  'storage2', 'unallocated']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
            'available': forms.Select(attrs={'class': 'form-control'}, choices=((True, 'Yes'), (False, 'No'))),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'storage1': forms.TextInput(attrs={'class': 'form-control', 'type': 'range'}),
            'storage2': forms.TextInput(attrs={'class': 'form-control', 'type': 'range'})
        }
