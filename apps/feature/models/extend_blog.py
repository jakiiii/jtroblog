from django.db import models

from base.models import BaseModel
from apps.feature.utils import extend_image_directory_path


class ExtendBlog(models.Model):
    title = models.CharField(
        max_length=255
    )
    image = models.ImageField(
        upload_to=extend_image_directory_path
    )
    link = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=6,
        choices=BaseModel.StatusChoices.choices,
        default=BaseModel.StatusChoices.PUBLISHED
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_at',)
        verbose_name = "Extend Blog"
        verbose_name_plural = "Extend Blog"
        db_table = "db_extend_blog"
