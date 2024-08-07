# Generated by Django 5.0.6 on 2024-07-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0010_remove_blog_created_at_en_remove_blog_created_at_tr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo1', models.ImageField(blank=True, null=True, upload_to='dimg')),
                ('logo2', models.ImageField(blank=True, null=True, upload_to='dimg')),
                ('title', models.CharField(max_length=30)),
                ('title_tr', models.CharField(max_length=30, null=True)),
                ('title_en', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=255)),
                ('description_tr', models.CharField(max_length=255, null=True)),
                ('description_en', models.CharField(max_length=255, null=True)),
                ('keywords', models.CharField(max_length=255)),
                ('keywords_tr', models.CharField(max_length=255, null=True)),
                ('keywords_en', models.CharField(max_length=255, null=True)),
                ('phohe_fixed', models.CharField(max_length=10)),
                ('phohe_mobil', models.CharField(max_length=10)),
                ('fax', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('Address', models.TextField()),
                ('postal_code', models.CharField(max_length=7)),
                ('facebook_url', models.URLField(max_length=255)),
                ('instagram_url', models.URLField(max_length=255)),
                ('youtube_url', models.URLField(max_length=255)),
                ('x_url', models.URLField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, max_length=30),
        ),
    ]
