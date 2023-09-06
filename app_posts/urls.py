from django.urls import path

from app_posts.views import CreatePostView, DeletePostView, EditPostView,detail_and_comment_post_view


urlpatterns = [
    path('post-create/', CreatePostView.as_view(), name='post create page'),
    path('post-edit/<int:pk>/', EditPostView.as_view(), name='post edit page'),
    path('post-delete/<int:pk>/', DeletePostView.as_view(), name='post delete page'),
    path('post-details/<int:pk>', detail_and_comment_post_view, name='details and comment page'),
]
