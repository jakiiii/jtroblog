from django.contrib import admin
from apps.blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_feature', 'is_trending', 'published']
    list_filter = ['author__username', 'published', 'is_feature', 'is_trending', 'status']
    search_fields = ['title', 'author', 'is_feature', 'is_trending']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'published'
    ordering = ['status', 'published']
