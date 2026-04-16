from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    # Validação:
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            raise forms.ValidationError('O valor do carro não pode ser menor que 20.000,00!')
        return value

    # Tambem pode ser feito assim: sel.add_error('value', 'O valor do carro não pode ser menor que 20.000,00!') para adicionar um erro específico ao campo value, sem precisar levantar uma exceção de validação.

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:  # O primeiro carro foi inventado em 1886
            raise forms.ValidationError('O ano de fabricação do carro não pode ser menor que 1975!')
        return factory_year