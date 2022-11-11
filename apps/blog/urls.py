from django.urls import path
from apps.blog.views import (
    HomeView, PostDetailView
)

app_name = 'blog'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/', PostDetailView.as_view(), name='post-detail'),
]
