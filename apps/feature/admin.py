from django.contrib import admin

from apps.feature.models import SocialMedia, ExtendBlog


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    pass


@admin.register(ExtendBlog)
class ExtendBlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
