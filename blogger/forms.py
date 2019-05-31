from django.forms import forms
from .models import Blogger

class BloggerForm(forms.ModelForm):
    class Meta:
        model = Blogger
        fields = "__all__"
