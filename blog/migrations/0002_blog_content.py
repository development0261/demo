# Generated by Django 3.1.3 on 2021-06-18 11:28

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
