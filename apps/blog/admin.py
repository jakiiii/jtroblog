from django.contrib import admin
from apps.blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_feature', 'is_trending', 'published']
    list_filter = ['is_feature', 'is_trending']
    search_fields = ['title', 'author', 'is_feature', 'is_trending']
