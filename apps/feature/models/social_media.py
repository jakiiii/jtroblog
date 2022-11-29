from django.db import models


class SocialMedia(models.Model):
    facebook = models.URLField(
        max_length=300,
        null=True,
        blank=True
    )
    twitter = models.URLField(
        max_length=300,
        null=True,
        blank=True
    )
    instagram = models.URLField(
        max_length=300,
        null=True,
        blank=True
    )
    linkedin = models.URLField(
        max_length=300,
        null=True,
        blank=True
    )
    pintest = models.URLField(
        max_length=300,
        null=True,
        blank=True
    )
    youtube = models.URLField(
        max_length=300,
        null=True,
        blank=True
    )
    stack_overflow = models.URLField(
        max_length=300,
        null=True,
        blank=True
    )
    dev_to = models.URLField(
        max_length=300,
        null=True,
        blank=True
    )
    figma = models.URLField(
        max_length=300,
        null=True,
        blank=True
    )
    medium = models.URLField(
        max_length=300,
        null=True,
        blank=True
    )
    github = models.URLField(
        max_length=300,
        null=True,
        blank=True
    )
    gitlab = models.URLField(
        max_length=300,
        null=True,
        blank=True
    )
    bitbucket = models.URLField(
        max_length=300,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return "Social Media"

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"
        db_table = "db_social_media"
