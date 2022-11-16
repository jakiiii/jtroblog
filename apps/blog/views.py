from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from apps.blog.models import Post


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'post_context'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = "Home"
        return context

    def get_queryset(self):
        return Post.objects.filter(status=Post.StatusChoices.PUBLISHED)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['title'] = "Post Detail"
        return context
