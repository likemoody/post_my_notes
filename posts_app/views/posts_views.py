import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.views.generic.base import View

from postmynotes.utils import *
from ..forms import CreatePostForm, AddCommentForm
from ..models import Post, Comment


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  # note ?


class AllPostsView(View):
    def get(self, request):
        form = CreatePostForm()
        posts = QueryPosts.query_posts(Post, banned=False)
        return render(request, 'posts_app/home.html', locals())

    def post(self, request):
        form = CreatePostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            title = form.cleaned_data.get('title')
            date_posted = datetime.datetime.now()
            author = User.objects.get(pk=request.user.id)
            Post.objects.create(content=content,
                                date_posted=date_posted,
                                author=author,
                                title=title,
                                banned=False)
        return redirect('home')


class PostDetailsView(View):
    def get(self, request, post_id):
        add_comment_form = AddCommentForm()
        post = Post.objects.get(pk=post_id)
        return render(request, 'posts_app/post_details.html', locals())

    def post(self, request, post_id):
        add_comment_form = AddCommentForm(request.POST)
        if add_comment_form.is_valid():
            content = add_comment_form.cleaned_data.get('content')
            date_posted = datetime.datetime.now()
            author = User.objects.get(pk=request.user.id)
            Comment.objects.create(content=content, date_posted=date_posted, author=author, post_id=post_id)
        return redirect('post-details', post_id=post_id)
