from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

from base.models import BaseModel

from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

from apps.about.utils import about_image_directory_path
User = settings.AUTH_USER_MODEL


class About(models.Model):
    title = models.CharField(
        max_length=255
    )
    description = RichTextUploadingField()
    image = models.ImageField(
        upload_to=about_image_directory_path,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
        indexes = [
            models.Index(fields=['title']),
        ]
        db_table = "db_about"
