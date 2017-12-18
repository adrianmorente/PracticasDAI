# restaurantes/forms.py

from django import forms
from django.core.exceptions import ValidationError

def valida_codigo_postal(value):
    if value < 10000 or value > 99999:
        raise ValidationError('%s no parece ser un código postal' % value)

def valida_numero_edificio(value):
    if value < 1 or value > 5000:
        raise ValidationError('Tan solo existen números de edificio entre 0 y 5000')

class RestauranteForm(forms.Form):
    name = forms.CharField(
        label = 'Nombre',
        max_length = 60,
        strip = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control col-md-4',
                'size' : 30,
                'placeholder' : 'Casa Morente'
            }
        ),
        required = True
    )

    borough = forms.CharField(
        label = 'Barrio',
        max_length = 80,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control col-md-4',
                'size' : 30,
                'placeholder' : 'Maracena'
            }
        ),
        required = True
    )

    cuisine = forms.CharField(
        label = 'Tipo de cocina',
        max_length = 80,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control col-md-4',
                'size' : 30,
                'placeholder' : 'Comida basura'
            }
        ),
        required = True
    )

    street = forms.CharField(
        label = 'Calle',
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control col-md-4',
                'size' : 30,
                'placeholder' : 'Gran Vía'
            }
        ),
        required = True
    )

    building = forms.IntegerField(
        label = 'Edificio',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control col-md-4',
                'size' : 30,
                'placeholder' : '1'
            }
        ),
        validators = [valida_numero_edificio]
    )

    zipcode = forms.IntegerField(
        label = 'Código Postal',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control col-md-4',
                'size' : 30,
                'placeholder' : '18001'
            }
        ),
        validators = [valida_codigo_postal]
    )
