# Generated by Django 2.2.1 on 2019-05-09 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('write', '0003_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_url',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, upload_to='blog_image/'),
        ),
    ]
