from django import forms
from .models import Brand

class CarForm(forms.Form):
    model = forms.CharField(max_length=100, required=True)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField(required=True)
    model_year = forms.IntegerField(required=True)
    plate = forms.CharField(max_length=10, required=False)
    value = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    photo = forms.ImageField(required=False)
