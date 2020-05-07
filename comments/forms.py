from django import forms
from .models import Comment


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
