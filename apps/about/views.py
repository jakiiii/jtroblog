from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from taggit.models import Tag

from base.models import BaseModel
from apps.blog.models import Post
from apps.category.models import Category
from apps.feature.models import SocialMedia, ExtendBlog
from apps.about.models import About


class AboutView(ListView):
    model = About
    template_name = 'about/about.html'
    context_object_name = 'about_context'

    def get_queryset(self):
        return About.objects.last()

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['title'] = "About"
        context['feature_post'] = Post.objects.filter(is_feature=True, status=Post.StatusChoices.PUBLISHED).order_by('-created_at')[:5]
        context['category_context'] = Category.objects.filter(status=BaseModel.StatusChoices.PUBLISHED).order_by('name')
        context['socialmedia'] = SocialMedia.objects.last()
        context['extend_blog_context'] = ExtendBlog.objects.filter(status=BaseModel.StatusChoices.PUBLISHED).order_by('-created_at')[:10]
        context['tag_context'] = Tag.objects.all().order_by('name')
        return context
