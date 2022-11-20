from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

from base.models import BaseModel

from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

from apps.blog.utils import post_image_directory_path
User = settings.AUTH_USER_MODEL


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status=Post.StatusChoices.PUBLISHED)


class Post(BaseModel):
    author = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='blog_post'
    )
    title = models.CharField(
        max_length=255,
    )
    category = models.ForeignKey(
        'category.Category',
        on_delete=models.CASCADE,
        related_name='categories'
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
    publish = models.DateTimeField(
        default=timezone.now
    )
    slug = models.SlugField(
        max_length=500,
        unique_for_date='publish'
    )
    status = models.CharField(
        max_length=6,
        choices=BaseModel.StatusChoices.choices,
        default=BaseModel.StatusChoices.PUBLISHED
    )
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={
            'slug': self.slug,
            'year': self.publish.year,
            'month': self.publish.month,
            'day': self.publish.day
        })

    class Meta:
        ordering = ('-publish',)
        indexes = [
            models.Index(fields=['-publish']),
        ]
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        db_table = "db_blog"
