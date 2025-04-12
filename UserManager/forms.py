# forms.py
from django import forms
from .models import UserAccount

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['name', 'email', 'password', 'role']

        widgets = {
            'published_date': forms.SelectDateWidget,
        }