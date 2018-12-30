from django import forms
from django.contrib.auth.models import User

from .models import Post, Message, Comment


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class SendMessageForm(forms.ModelForm):
    user_to = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['user_to', 'content']
        labels = {
            'user_to': '',
            'content': '',
        }

    # def __init__(self, uid, *args, **kwargs):
    #     super(SendMessageForm, self).__init__(*args, **kwargs)
    #     self.fields['user_to'].queryset = User.objects.exclude(
    #         pk=uid)


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
