import os
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from app_common.forms import CommentForm
from app_posts.forms import CreatePostForm, DeletePostForm

from app_posts.models import Post

class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('index page')
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.to_user = self.request.user
        instance.save()
        return super().form_valid(form)


class EditPostView(UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('index page')


def detail_and_comment_post_view(request, pk):
    current_post = Post.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_post = current_post
            comment.to_user = request.user
            comment.save()
            return redirect('index page')
    context = {
        'form': form,
        'current_post': current_post,
    }
       
    return render(request, 'posts/details_and_comment.html', context)

class DeletePostView(DeleteView):
    model = Post
    form_class = DeletePostForm
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('index page')

   