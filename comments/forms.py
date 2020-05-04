from django import forms
from .models import Comment


class CreateCommentForm(forms.ModelForm):
    text = models.TextField()

    class Meta:
        model = Comment
        fields = ["text"]


class EditCommentForm(forms.ModelForm):
    text = models.TextField()

    class Meta:
        model = Comment
        fields = ["text"]
