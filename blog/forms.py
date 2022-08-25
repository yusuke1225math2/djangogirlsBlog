from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta(forms.ModelForm):
        model = Post
        fields = ('title', 'text',)
