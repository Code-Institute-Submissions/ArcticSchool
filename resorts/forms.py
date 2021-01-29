"""
These is a form which will be displayed in
user management section when user is super user
to manage resorts without using admin page
"""
from django import forms
from .models import Resort


class ResortForm(forms.ModelForm):
    """ Resort form """
    class Meta:
        model = Resort
        fields = ('name', 'country', 'about',
                  'open_season', 'top_altitude',
                  'bottom_altitude', 'resort_altitude',
                  'levels', 'instructors', 'image',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Resort Name',
            'country': 'Country',
            'about': 'About',
            'open_season': 'Open Season (Month - Month)',
            'top_altitude': 'Top Altitude',
            'bottom_altitude': 'Bottom Altitude',
            'resort_altitude': 'Resort Altitude',
            'levels': 'Expected Levels (Advanced, Example, etc.)',
            'instructors': 'Instructors',
            'image': 'Image',
        }

        self.fields['about'].widget.attrs = {'rows': 3}
        self.fields['levels'].widget.attrs = {'rows': 1}
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            if field == 'image' or field == 'country':
                self.fields[field].widget.attrs['placeholder'] = False
            else:
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'add-form-input'
            self.fields[field].label = False
