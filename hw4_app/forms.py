from django import forms

from hw4_app.models import Product

class FormProductAdd(forms.Form):
    name = forms.CharField(max_length=50,
            widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Название товара'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': 'Описание'}))
    price = forms.FloatField(min_value=0.0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Цена'}))
    prod_quant = forms.IntegerField(min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Количество'}))
    img = forms.ImageField()


class FormProductsUpdate(forms.Form):
    product = forms.ModelChoiceField(
        label='Товар',
        queryset=Product.objects.all(), 
        empty_label='Выберите товар')
    name = forms.CharField(
        max_length=50, 
        label='Название', 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Название товара'})
    )
    description = forms.CharField(
        label='Описание', 
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': 'Описание'}))
    price = forms.FloatField(
        min_value=0.0, 
        label='Цена', 
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Цена'}))
    prod_quant = forms.IntegerField(
        min_value=0, 
        label='Количество', 
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Количество'}))
    img = forms.ImageField(
        label='Изображение',
        required=False)