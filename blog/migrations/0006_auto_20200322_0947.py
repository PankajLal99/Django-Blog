# Generated by Django 3.0.2 on 2020-03-22 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200321_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, default='', null=True, upload_to='pictures'),
        ),
    ]
