from django.contrib import admin
from apps.category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['status']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
