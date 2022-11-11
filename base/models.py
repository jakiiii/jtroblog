from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class BaseModel(models.Model):
    class StatusChoices(models.TextChoices):
        PUBLISHED = 'published', _('published')
        UNPUBLISHED = 'unpublished', _('unpublished')
        POSTPONED = 'postponed', _('postponed')
        ARCHIVED = 'archived', _('archived')

    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="post_create")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="post_update")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        app_label = 'base'
