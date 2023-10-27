from .models import Comment
from django import forms


#class ReviewForm(forms.ModelForm):
#    class Meta:
#        model = Review
#        fields = ('content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)	

class GameFilterForm(forms.Form):
    platform = forms.CharField(required=False)
    year = forms.CharField(required=False)