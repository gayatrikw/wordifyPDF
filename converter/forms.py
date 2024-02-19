# converter/forms.py
from django import forms
from .models import ConvertedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = ConvertedFile
        fields = ['file']
