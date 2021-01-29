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
        placeholders = {
            'name': 'Category Name',
            'friendly_name': 'Category Visible Name',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'add-form-input'
            self.fields[field].label = False


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

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Lesson Name',
            'category': 'Category',
            'level': 'Level',
            'description': 'Description',
            'start_date': 'Starting Date',
            'end_date': 'Finishing Datae',
            'start_time': 'Start Time',
            'end_time': 'End Time',
            'participants': 'Participants',
            'resort': 'Resort',
            'price': 'Price',
            'supper_offer': 'Supper Offer',
            'image': 'Image',
        }

        self.fields['description'].widget.attrs = {'rows': 3}
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            if field == 'image' or field == 'level' or field == 'resort' or field =='category' or field =='supper_offer':
                self.fields[field].widget.attrs['placeholder'] = False
            else:
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'add-form-input'
            self.fields[field].label = False
