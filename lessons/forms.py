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


class LessonsForm(forms.ModelForm):
    """ Lessons form """
    class Meta:
        model = Lesson
