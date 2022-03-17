from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '4',
            'placeholder': 'write a post about something...'
            }))

    class Meta:
        model = Post
        fields = ['body']