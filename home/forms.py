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
        self.fields['title'].widget.attrs = {'rows': 1}
        self.fields['description'].widget.attrs = {'rows': 3}
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = '...'
            self.fields[field].widget.attrs['class'] = 'add-form-input'


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
        self.fields['title'].widget.attrs = {'rows': 1}
        self.fields['description'].widget.attrs = {'rows': 3}
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'level':
                self.fields[field].widget.attrs['placeholder'] = False
            else:
                self.fields[field].widget.attrs['placeholder'] = '...'
            self.fields[field].widget.attrs['class'] = 'add-form-input'


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
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'url':
                self.fields[field].widget.attrs['placeholder'] = '...'
            else:
                self.fields[field].widget.attrs['placeholder'] = False
            self.fields[field].widget.attrs['class'] = 'add-form-input'
