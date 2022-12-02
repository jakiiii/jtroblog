from django import template
from django.utils.safestring import mark_safe

import markdown

from apps.blog.models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('base/latest.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.filter(status=Post.StatusChoices.PUBLISHED).order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


# @register.simple_tag
# def get_most_commented_post(count=5):
#     return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
