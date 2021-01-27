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
