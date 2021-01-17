from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'postcode': 'Postcode',
            'country': 'Country',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fiedls[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].wdiget.attrs['placeholder'] = placeholder
            self.fields[field].wdiget.attrs['class'] = 'stripe-style-input'
            self.fields[field].lablel = False