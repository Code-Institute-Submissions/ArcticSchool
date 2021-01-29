"""
These are forms which will be displayed in
user management section when user is super user
to manage different categories and lessons
without using admin page
"""

from django import forms
from .models import Category, Lesson


class CategoriesForm(forms.ModelForm):
    """ Categories form """
    class Meta:
        model = Category
        fields = ('name', 'friendly_name',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = '...'
            self.fields[field].widget.attrs['class'] = 'add-form-input'


class LessonsForm(forms.ModelForm):
    """ Lessons form """
    class Meta:
        model = Lesson
        fields = (
            'name', 'category', 'level',
            'description', 'start_date', 'end_date',
            'start_time', 'end_time', 'participants',
            'resort', 'price', 'supper_offer', 'image',
        )
        labels = {
            'image':'Add Image',
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': '...',
            'category': '...',
            'level': '...',
            'description': '...',
            'start_date': 'YYYY-MM-DD',
            'end_date': 'YYYY-MM-DD',
            'start_time': 'HH:MM:SS',
            'end_time': 'HH:MM:SS',
            'participants': 'Number of Participants',
            'resort': '...',
            'price': '150',
            'supper_offer': 'Yes/No',
            'image': '...',
        }

        self.fields['description'].widget.attrs = {'rows': 3}
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            if field == 'image' or field == 'level' or field == 'resort' or field =='category' or field =='supper_offer':
                self.fields[field].widget.attrs['placeholder'] = False
            else:
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'add-form-input'
