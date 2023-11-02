# social/forms.py
from django import forms
from .models import UserProfilePost

class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserProfilePost
        fields = ['content']
