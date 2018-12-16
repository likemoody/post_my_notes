from django.db import models
from django.urls.base import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-details', kwargs={'pk': self.pk})


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
    content = models.TextField()
    user_from = models.ForeignKey(User, on_delete=models.CASCADE,  # todo? CASCADE
                                  related_name='messages_sent')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='messages_received')
    is_read = models.BooleanField()

    def __str__(self):
        return f'Message: {self.user_from} >> {self.user_to}'
