from .models import *
from django import forms

class ContributeForm(forms.ModelForm):

    class Meta:
        model = Contribute
        fields = ('blog_title', 'short_description', 'blog_content', 'your_name', 'email', 'about_yourself', 'facebook_profile_link',)


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ('name', 'email', 'message',)