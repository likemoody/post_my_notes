from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.base import View

from posts_app.models import Post
from ..forms import UserUpdateForm, ProfileUpdateForm


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, uid):
        posts = Post.objects.filter(author_id=uid).order_by('-date_posted')
        user_profile = User.objects.get(pk=uid)
        return render(request, 'profile_view.html', locals())


class UserProfileEditView(LoginRequiredMixin, View):
    def get(self, request):
        user_profile = User.objects.get(pk=request.user.id)
        user_form = UserUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
        profile_form = ProfileUpdateForm(instance=request.user)
        return render(request, 'profile_edit.html', locals())

    def post(self, request):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid() and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)                        # note important! To keep user logged in.
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile-view', uid=request.user.id)
        return render(request, 'profile_edit.html', locals())


