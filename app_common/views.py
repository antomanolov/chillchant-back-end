from django.shortcuts import redirect, render
from app_common.models import Like

from app_posts.models import Post

def like_view(request, pk):
    current_post = Post.objects.filter(pk=pk).get()
    liked = current_post.user_has_liked(request.user)
    if not liked:
        like = Like()
        like.to_post = current_post
        like.to_user = request.user
        like.save()
    else:
        like = Like.objects.filter(to_user_id=request.user, to_post_id=current_post)
        like.delete()
    return redirect(request.META['HTTP_REFERER'])
