from django.db import models
from django.urls.base import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    banned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('post-details', kwargs={'pk': self.pk})  # to redirect to newly created post
        return reverse('home')


class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='post_comments')

    def __str__(self):
        return f'Comment: {self.post}'


class Message(models.Model):
    content = models.TextField(max_length=60)
    date_sent = models.DateTimeField(default=timezone.now)
    date_read = models.DateTimeField(default=timezone.now, null=True)
    user_from = models.ForeignKey(User, on_delete=models.CASCADE,  # note to let message have sender and receiver
                                  related_name='messages_sent')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='messages_received')
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message: {self.user_from} >> {self.user_to}'
