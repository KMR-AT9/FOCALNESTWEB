# Generated by Django 4.2.7 on 2023-11-19 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FocalNest', '0022_remove_gallery_images_delete_galleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='images',
            field=models.ImageField(default=1, upload_to='gallery_images/'),
            preserve_default=False,
        ),
    ]
