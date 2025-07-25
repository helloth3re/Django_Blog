# Generated by Django 5.2.1 on 2025-05-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_banner_alter_post_categories_alter_post_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='slug',
            field=models.SlugField(blank=True, max_length=270),
        ),
        migrations.AlterField(
            model_name='banner',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
