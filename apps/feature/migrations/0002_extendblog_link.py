# Generated by Django 4.1.3 on 2022-11-29 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendblog',
            name='link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]