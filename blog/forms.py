from .models import *
from django import forms

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Travel
        fields = ('image',)