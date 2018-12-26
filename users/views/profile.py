from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.base import View

from posts_app.models import Post
from ..forms import UserUpdateForm


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, uid):
        posts = Post.objects.filter(author_id=uid).order_by('-date_posted')
        user_profile = User.objects.get(pk=uid)
        return render(request, 'profile_view.html', locals())


class UserProfileEditView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        p_form = PasswordChangeForm(request.user)
        return render(request, 'profile_edit.html', locals())

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid() and p_form.is_valid():
            user = p_form.save()
            form.save()
            update_session_auth_hash(request, user)                         # note important! To keep user logged in.
            messages.success(request, 'Profile updated successfully')
            return redirect('profile-view')
        return render(request, 'profile_edit.html', locals())
