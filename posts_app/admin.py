from django.contrib import admin
from .models import Post, Comment, Message

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Message)


def short_content(text):
    return str(text.content)[0:25]


def block(model_admin, request, query_set):
    query_set.update(blocked=True)


@admin.register(Post)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['title', short_content, "author", "date_posted", "banned"]
    list_filter = ["author", "date_posted", "banned"]
    actions = [block, ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["user_from", "user_to", short_content, "date_sent", "is_read"]
    list_filter = ["user_from", "user_to", "date_sent", "is_read"]
    # actions = [block, ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', short_content, 'date_posted']
    list_filter = ["author", "date_posted"]
    # actions = [block, ]
