# Generated by Django 4.0.4 on 2022-05-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0010_faculty_lastupdated'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoiInitiative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logoImg', models.FileField(upload_to='goi')),
                ('goiLink', models.URLField(max_length=500, null=True)),
            ],
        ),
    ]
