# Generated by Django 4.0.5 on 2022-06-09 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_blogindexgalleryimage_blogindexpagegalleryimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpagegalleryimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogpagegalleryimage',
            name='page',
        ),
        migrations.DeleteModel(
            name='BlogIndexPageGalleryImage',
        ),
        migrations.DeleteModel(
            name='BlogPageGalleryImage',
        ),
    ]
