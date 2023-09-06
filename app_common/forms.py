from django import forms

from app_common.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('to_user', 'to_post',)