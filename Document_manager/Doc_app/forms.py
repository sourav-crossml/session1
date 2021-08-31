from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    """
    this form will help in geeting user input file
    """
    class Meta:
        model = Document
        fields = ('description','document')