# Generated by Django 5.0.6 on 2024-07-23 11:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0005_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='content_tr',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title_tr',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
