from django import forms
from .models import Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 0:
            raise forms.ValidationError("O valor não pode ser negativo.")
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1886:  # O primeiro carro foi inventado em 1886
            raise forms.ValidationError("O ano de fabricação não pode ser anterior a 1886.")
        return factory_year