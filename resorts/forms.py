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
        labels = {
            'image': 'Add Image',
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': '...',
            'country': '...',
            'about': '...',
            'open_season': 'Open Season (Month - Month)',
            'top_altitude': '...',
            'bottom_altitude': '...',
            'resort_altitude': '...',
            'levels': 'Expected Levels (Advanced, Example, etc.)',
            'instructors': '...',
            'image': '...',
        }

        self.fields['about'].widget.attrs = {'rows': 3}
        self.fields['levels'].widget.attrs = {'rows': 1}
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            if field == 'image' or field == 'country':
                self.fields[field].widget.attrs['placeholder'] = False
            else:
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'add-form-input'
