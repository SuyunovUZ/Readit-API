from django.urls import path

from .views import *

urlpatterns = [
    path('home/', HomeAPIView.as_view(), name='home'),
    path('posts/<int:pk>/', DetailAPIView.as_view(), name='detail'),
    path('posts/', PostAPIView.as_view(), name='posts'),
    path('about/', AboutAPIView.as_view(), name='about'),
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('tags/', TagAPIView.as_view(), name='tags'),
    path('authors/', AuthorAPIView.as_view(), name='authors'),
    path('happy-clients/', HappyClientsAPIView.as_view(), name='clients'),
    path('comments/', CommentAPIView.as_view(), name='comments'),
    path('recent/', RecentBlogsAPIView.as_view(), name='recent-posts'),
]