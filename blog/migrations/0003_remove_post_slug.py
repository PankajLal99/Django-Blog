# Generated by Django 3.0.2 on 2020-03-21 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]