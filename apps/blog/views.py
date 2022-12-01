from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail

from taggit.models import Tag

from base.models import BaseModel
from apps.blog.models import Post
from apps.category.models import Category
from apps.feature.models import SocialMedia, ExtendBlog

from apps.blog.forms import EmailPostForm

EMAIL_ACCOUNT = settings.EMAIL_HOST_USER

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'post_context'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = "Home"
        context['trending_post'] = Post.objects.filter(is_trending=True, status=Post.StatusChoices.PUBLISHED).order_by('-created_at')[:10]
        context['slider_context'] = Post.objects.filter(is_cover=True, status=Post.StatusChoices.PUBLISHED).order_by('-created_at')[:3]
        context['feature_post'] = Post.objects.filter(is_feature=True, status=Post.StatusChoices.PUBLISHED).order_by('-created_at')[:5]
        context['category_context'] = Category.objects.filter(status=BaseModel.StatusChoices.PUBLISHED).order_by('name')
        context['socialmedia'] = SocialMedia.objects.last()
        context['extend_blog_context'] = ExtendBlog.objects.filter(status=BaseModel.StatusChoices.PUBLISHED).order_by('-created_at')[:10]
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


def post_share(request, slug):
    template_name = "blog/snippets/share.html"
    post = get_object_or_404(Post, slug=slug, status=Post.StatusChoices.PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read" f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, EMAIL_ACCOUNT, [cd['to']])
    else:
        form = EmailPostForm()
    sent = True
    context = {
        'post': post,
        'form': form,
        'send': sent
    }
    return render(request, template_name, context)
