from django.urls import path

from .views import posts_views

urlpatterns = [
    path('', posts_views.AllPostsView.as_view(), name='home'),
    path('create-post/', posts_views.CreatePostView.as_view(), name='create-post')
]
