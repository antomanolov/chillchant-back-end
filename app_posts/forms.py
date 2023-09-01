from django import forms

from app_posts.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('to_user', )


class DeletePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('text', 'image', 'to_user')