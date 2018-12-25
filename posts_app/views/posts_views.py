from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.base import View

from ..forms import CreatePostForm
from ..models import Post


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)                                             # note ?


class AllPostsView(View):
    def get(self, request):
        form = CreatePostForm()
        posts = Post.objects.all().order_by('-date_posted')
        return render(request, 'posts_app/home.html', locals())


class PostDetailsView(View):
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        return render(request, 'posts_app/post_details.html', locals())
