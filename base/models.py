from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

User = settings.AUTH_USER_MODEL


class BaseModel(models.Model):
    class StatusChoices(models.TextChoices):
        PUBLISHED = 'PUB', _('Published')
        UNPUBLISHED = 'UNPUB', _('Unpublished')
        DRAFT = 'DR', _('Draft')
        ARCHIVED = 'ARC', _('Archived')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        app_label = 'base'
