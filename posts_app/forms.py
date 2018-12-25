from django import forms
from .models import Post, Message


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['user_to', 'content']
        labels = {
            'user_to': 'Send message',
            'content': '',
        }
