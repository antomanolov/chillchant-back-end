from django.urls import path

from app_posts.views import CreatePostView


urlpatterns = [
    path('post-create/', CreatePostView.as_view(), name='post create page'),
]
