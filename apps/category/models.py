from django.db import models

from base.models import BaseModel


class Category(models.Model):
    name = models.CharField(
        max_length=100,
    )
    slug = models.SlugField(
        max_length=120,
    )
    status = models.CharField(
        max_length=6,
        choices=BaseModel.StatusChoices.choices,
        default=BaseModel.StatusChoices.PUBLISHED
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Category"
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name_plural = "Categories"
        db_table = "db_category"
