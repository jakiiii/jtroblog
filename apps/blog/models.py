from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from base.models import BaseModel

from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

from apps.blog.utils import post_image_directory_path
User = get_user_model()


class Post(BaseModel):
    author = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='blog_post'
    )
    title = models.CharField(
        max_length=255,
    )
    cover = models.ImageField(
        upload_to=post_image_directory_path,
        null=True,
        blank=True
    )
    description = RichTextUploadingField()
    is_feature = models.BooleanField(
        default=False
    )
    is_trending = models.BooleanField(
        default=False
    )
    tags = TaggableManager()
    slug = models.SlugField(
        max_length=500
    )
    published = models.DateTimeField(
        default=timezone.now
    )
    status = models.CharField(
        max_length=6,
        choices=BaseModel.StatusChoices.choices,
        default=BaseModel.StatusChoices.PUBLISHED
    )

    def __str__(self):
        return self.tags

    class Meta:
        ordering = ('-published',)
        indexes = [
            models.Index(fields=['-published']),
        ]
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        db_table = "db_blog"
