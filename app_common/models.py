from django.db import models
from app_posts.models import Post

from app_profiles.appuser import AppUser

class Like(models.Model):
    to_user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    to_post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes',

    )

    def __str__(self):
        return f'You\'ve liked this post'

class Comment(models.Model):
    text = models.TextField()
    to_user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )
    to_post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    def __str__(self):
        return f'You\'ve commented on post'
