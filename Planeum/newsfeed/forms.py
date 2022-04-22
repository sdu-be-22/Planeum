from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '4',
            'placeholder': 'write a post about something...'
            }))
    
    image = forms.ImageField(required=False)
    
    class Meta:
        model = Post
        fields = ['body', 'image']
        

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '4',
            'placeholder': 'write a comment...'
        }))

    class Meta:
        model = Comment
        fields = ['comment']
