# Generated by Django 4.1.3 on 2022-11-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_cover',
            field=models.BooleanField(default=False),
        ),
    ]
