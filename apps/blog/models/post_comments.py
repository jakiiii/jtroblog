from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

from base.models import BaseModel

from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

from apps.blog.utils import post_image_directory_path
User = settings.AUTH_USER_MODEL


class Comment(BaseModel):
    post = models.ForeignKey(
        'blog.Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(
        max_length=100
    )
    email = models.EmailField(
        max_length=32
    )
    body = models.TextField()
    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at'])
        ]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
