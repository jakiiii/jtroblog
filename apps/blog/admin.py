from django.contrib import admin
from apps.blog.models import Post, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'created_at', 'name', 'email', 'active']
    list_filter = ['active', 'created_at']
    search_fields = ['name', 'email', 'body']


class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInlineAdmin]
    list_display = ['title', 'author', 'is_feature', 'is_trending', 'publish']
    list_filter = ['author__username', 'publish', 'is_feature', 'is_trending', 'status']
    search_fields = ['title', 'author', 'is_feature', 'is_trending']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
