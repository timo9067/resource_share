# Generated by Django 4.2.4 on 2023-08-31 08:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0007_resourcestag_resource_tag_unique'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rating',
            new_name='ResourcesRating',
        ),
    ]