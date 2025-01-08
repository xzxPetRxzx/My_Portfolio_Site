from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ваш комментарий...'}),
        }
