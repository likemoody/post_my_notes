from django import forms
from .models import Post, Message, Comment


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['user_to', 'content']
        labels = {
            'user_to': '',
            'content': '',
        }


class SendMessageToForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        labels = {
            'content': '',
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': ''
        }

