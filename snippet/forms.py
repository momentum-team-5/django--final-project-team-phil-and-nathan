from django import forms
# from django.core.exceptions import ValidationError
from .models import Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = [
            'title',
            'body'
        ]