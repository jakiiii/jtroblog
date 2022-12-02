from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity

from taggit.models import Tag

from base.models import BaseModel
from apps.blog.models import Post, Comment
from apps.category.models import Category
from apps.feature.models import SocialMedia, ExtendBlog

from apps.blog.forms import EmailPostForm, CommentCreationForm, SearchForm

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
        post_tags_ids = self.get_object().tags.values_list('id', flat=True)
        context['similar_posts'] = Post.published.filter(tags__in=post_tags_ids).exclude(id=self.get_object().id)
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


def post_search(request):
    template_name = 'blog/snippets/search.html'
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # search_vector = SearchVector('title', 'description')
            search_vector = SearchVector('title', weight='A')  + SearchVector('description', weight='B')
            search_query = SearchQuery(query)
            # results = Post.published.annotate(search=search_vector,rank=SearchRank(search_vector, search_query)).filter(rank__gte=0.3).order_by('-rank')
            #######################
            # psql db_jblog
            # CREATE EXTENSION pg_trgm;
            # CREATE EXTENSION
            # import method in views.py
            # from django.contrib.postgres.search import TrigramSimilarity
            ########################
            results = Post.published.annotate(similarity=TrigramSimilarity('title', query)).filter(similarity__gt=0.1).order_by('-similarity')


    context = {
        'form': form,
        'query': query,
        'results': results
    }
    return render(request, template_name, context)
