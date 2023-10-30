from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form model that allows authenticated users to write and submit comments
    """
    class Meta:
        model = Comment
        fields = ('body',)


class GameFilterForm(forms.Form):
    """
    Form model that allows users to filter games
    """
    platform = forms.CharField(required=False)
    year = forms.CharField(required=False)
