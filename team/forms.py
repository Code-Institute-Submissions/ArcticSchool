"""
These is a form which will be displayed in
user management section when user is super user
to manage team cards without using admin page
"""
from django import forms
from .models import InstructorProfile


class InstructorProfileForm(forms.ModelForm):
    """ Instructor profile form """
    class Meta:
        model = InstructorProfile
        fields = ('name', 'age', 'about', 'image',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name and Surname',
            'age': 'Age',
            'about': 'About Instructor',
            'image': 'Image',
        }

        self.fields['about'].widget.attrs = {'rows': 3}
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'add-form-input'
            self.fields[field].label = False
