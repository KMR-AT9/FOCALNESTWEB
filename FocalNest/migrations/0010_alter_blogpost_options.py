# Generated by Django 4.2.7 on 2023-11-15 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FocalNest', '0009_alter_blogpost_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'Custom Blog Post', 'verbose_name_plural': 'Custom Blog Posts'},
        ),
    ]
