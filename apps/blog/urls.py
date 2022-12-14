from django.urls import path
from apps.blog.views import (
    HomeView, PostDetailView, post_share, post_search
)
from apps.blog.feeds import LatestPostsFeed


app_name = 'blog'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<int:year>/<int:month>/<int:day>/<str:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('search/', post_search, name='post_search'),
    path('detail/<str:slug>/share/', post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]
