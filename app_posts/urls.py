from django.urls import path

from app_posts.views import CreatePostView, EditPostView


urlpatterns = [
    path('post-create/', CreatePostView.as_view(), name='post create page'),
    path('post-edit/<int:pk>/', EditPostView.as_view(), name='post edit page'),
]
