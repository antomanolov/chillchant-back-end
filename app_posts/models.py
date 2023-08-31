from django.db import models
from app_posts.validation_functions import image_size_validation

from app_profiles.appuser import AppUser

class Post(models.Model):
    text = models.TextField()
    image = models.ImageField(
        validators=(
            image_size_validation,
        ),
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    to_user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    def user_has_liked(self, user):
        return self.likes.filter(to_user=user).exists()
    
    def total_likes(self):
        return self.likes.count()
    
    def total_comments(self):
        return self.comments.count()

    