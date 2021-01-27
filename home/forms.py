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


class LevelCardsForm(forms.ModelForm):
    """ Lesson cards form """
    class Meta:
        model = LevelCard


class SocialMediaIconsForm(forms.ModelForm):
    """ Social media icons form """
    class Meta:
        model = SocialIcon
