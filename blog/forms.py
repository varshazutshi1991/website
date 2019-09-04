from .models import *
from django import forms

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Travel
        fields = ('image',)



class ContributeForm(forms.ModelForm):

    class Meta:
        model = Contribute
        fields = ('blog_title', 'short_description', 'blog_content', 'your_name', 'email', 'about_yourself', 'facebook_profile_link',)


# class UserContributionForm(forms.Form):
#     blog_title = forms.CharField(max_length=100, label="blog title")
#     short_description = forms.CharField(max_length=200, label="short description")
#     blog_content = forms.Textarea()
#     your_name = forms.CharField(max_length=50, label='user name')
#     email = forms.EmailField(label="Email Address", max_length=100)
#     about_yourself = forms.Textarea()
#     facebook_profile_link = forms.URLField(max_length=150)