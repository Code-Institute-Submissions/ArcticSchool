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
