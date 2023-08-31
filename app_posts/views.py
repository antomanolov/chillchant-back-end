
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from app_posts.forms import CreatePostForm

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
