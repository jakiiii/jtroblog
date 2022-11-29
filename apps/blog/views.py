from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from taggit.models import Tag

from base.models import BaseModel
from apps.blog.models import Post
from apps.category.models import Category


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'post_context'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = "Home"
        context['trending_post'] = Post.objects.filter(is_trending=True, status=Post.StatusChoices.PUBLISHED).order_by('-created_at')
        context['category_context'] = Category.objects.filter(status=BaseModel.StatusChoices.PUBLISHED).order_by('name')
        context['slider_context'] = Post.objects.filter(is_cover=True, status=Post.StatusChoices.PUBLISHED).order_by('-created_at')
        context['feature_post'] = Post.objects.filter(is_feature=True, status=Post.StatusChoices.PUBLISHED).order_by('-created_at')
        context['tag_context'] = Tag.objects.all().order_by('name')
        return context

    def get_queryset(self):
        return Post.objects.filter(status=Post.StatusChoices.PUBLISHED).order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['title'] = "Post Detail"
        return context
