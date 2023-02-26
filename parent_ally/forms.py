from django import forms
from .models import Posting


class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['title', 'content']
