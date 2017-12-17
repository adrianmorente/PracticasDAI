# restaurantes/forms.py

from django import forms
from django.core.exceptions import ValidationError

def valida_codigo_postal(value):
    if value < 10000 or value > 99999:
        raise ValidationError('%s no parece ser un código postal' % value)

def valida_edificio(value):
    if value < 1 or value > 5000:
        raise ValidationError('Tan solo existen números de edificio entre 0 y 5000')


class RestauranteForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=60, strip=True,
        widget=forms.TextInput(
            attrs={'class':'form-control text-muted col-md-4',
            'size':30,
            'placeholder':'el nombre que sea',
        }),
        validators=[valida_nombre])
    cuisine = forms.CharField(label='Tipo de cocina', max_length=80, required=True)
    street = forms.CharField(label='Calle', max_length=100, required=True)
    building = forms.IntegerField(label='Edificio', max_length=4, required=True, validators=[valida_numero_edificio])
    zipcode = forms.IntegerField(label='Código Postal', required=True, validators=[valida_codigo_postal])
