from django import forms
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.base import View

from ..forms import CreatePostForm
from ..models import Post


# class AllPostsView(ListView):
#     model = Post
#     template_name = 'posts_app/home.html'
#     ordering = ['-date_posted']
#     context_object_name = 'posts'


class CreatePostView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AllPostsView(View):
    def get(self, request):
        form = CreatePostForm()
        posts = Post.objects.all().order_by('-date_posted')
        return render(request, 'posts_app/home.html', locals())
