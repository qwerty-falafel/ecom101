from django.urls import path
from .views import news_feed, all_posts

urlpatterns = [
    path('feed/', news_feed, name='news_feed'),
    path('all_posts/', all_posts, name='all_posts'),
]
