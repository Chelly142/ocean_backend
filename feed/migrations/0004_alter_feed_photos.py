# Generated by Django 4.1.7 on 2023-03-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_alter_feed_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='photos',
            field=models.ImageField(blank=True, upload_to='feed/images', verbose_name='photos'),
        ),
    ]
