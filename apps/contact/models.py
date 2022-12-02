from django.db import models

from base.models import BaseModel
from apps.contact.utils import contact_image_directory_path

class ContactInfo(models.Model):
    title = models.CharField(
        max_length=100
    )
    body = models.TextField()
    image = models.ImageField(
        upload_to=contact_image_directory_path
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"
        indexes = [
            models.Index(fields=['title']),
        ]
        db_table = "db_contact_info"


class Contact(BaseModel):
    name = models.CharField(
        max_length=100
    )
    email = models.EmailField(
        max_length=32
    )
    subject = models.CharField(
        max_length=255
    )
    body = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['-created_at'])
        ]
        verbose_name = "Contact US"
        verbose_name_plural = "Contact US"
        db_table = "db_contact"
