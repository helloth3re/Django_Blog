from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'summary',
            'content',
            'post_display',
            'status',
            'categories',
            'tags',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Short summary', 'rows': 3}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
