# forms.py
from django import forms
from .models import AssignLevels

class AssignLevelsForm(forms.ModelForm):
    class Meta:
        model = AssignLevels
        fields = ['user', 'Level']

        # widgets = {
        #     'published_date': forms.SelectDateWidget,
        # }