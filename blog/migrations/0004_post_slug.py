# Generated by Django 5.1.7 on 2025-03-15 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='example-slug', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
