from django import forms
from notgur.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        fields = ("body", )
        model = Comment
