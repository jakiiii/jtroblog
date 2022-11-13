import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser

from apps.accounts.utils import user_photo_directory_path


class User(AbstractUser):
    uid = models.CharField(
        max_length=40,
        default=uuid.uuid4,
        unique=True,
        verbose_name=_("Unique ID")
    )
    photo = models.ImageField(
        upload_to=user_photo_directory_path,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'svg'])]
    )
    is_author = models.BooleanField(
        default=False
    )
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"
        db_table = "db_user"
