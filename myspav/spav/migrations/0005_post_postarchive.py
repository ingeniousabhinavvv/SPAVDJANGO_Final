# Generated by Django 4.0.4 on 2022-05-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0004_remove_gallery_gallerylink_gallery_gallerurl_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]