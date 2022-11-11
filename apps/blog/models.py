from django.db import models
from base.models import BaseModel

from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

from apps.blog.utils import post_image_directory_path


class Post(BaseModel):
    title = models.CharField(
        max_length=255,
    )
    cover = models.ImageField(
        upload_to=post_image_directory_path,
        null=True,
        blank=True
    )
    description = RichTextUploadingField()
    tags = TaggableManager()
    status = models.CharField(
        max_length=12,
        choices=BaseModel.StatusChoices.choices,
        default=BaseModel.StatusChoices.PUBLISHED
    )

    def __str__(self):
        return self.tags

    class Meta:
        ordering = ('created_at',)
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
