from django.contrib import admin

from apps.about.models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
