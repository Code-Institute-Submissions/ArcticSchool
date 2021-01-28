"""
These are forms which will be displayed in
user management section when user is super user
to manage different models without using admin page
"""

from django import forms
from .models import LessonCard, LevelCard, SocialIcon


class LessonCardsForm(forms.ModelForm):
    """ Lesson cards form """
    class Meta:
        model = LessonCard
        fields = ('title', 'description',
                  )

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'description': 'Description',
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


class LevelCardsForm(forms.ModelForm):
    """ Lesson cards form """
    class Meta:
        model = LevelCard
        fields = ('title', 'level',
                  'description',
                  )

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Level Card Name',
            'level': 'Level',
            'description': 'Description',
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


class SocialMediaIconsForm(forms.ModelForm):
    """ Social media icons form """
    class Meta:
        model = SocialIcon
        fields = ('name', 'icon', 'url',
                  )

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'icon': 'Icon',
            'url': 'Url Address',
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
