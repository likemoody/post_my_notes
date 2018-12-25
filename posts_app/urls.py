from django.urls import path

from .views import posts_views, messages_views

urlpatterns = [
    path('', posts_views.AllPostsView.as_view(), name='home'),
    path('create-post/', posts_views.CreatePostView.as_view(), name='create-post'),
    path('post/<int:post_id>', posts_views.PostDetailsView.as_view(), name='post-details'),
    path('messages/', messages_views.MessagesView.as_view(), name='messages'),
    path('message/<int:message_id>', messages_views.SingleMessageView.as_view(), name='message-single')
]
