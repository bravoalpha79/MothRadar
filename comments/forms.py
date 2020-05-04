from django import forms
from .models import Comment


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
