# Generated by Django 4.0.4 on 2022-05-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0011_goiinitiative'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goiinitiative',
            name='logoImg',
        ),
        migrations.AddField(
            model_name='goiinitiative',
            name='goiLogo',
            field=models.ImageField(null=True, upload_to='goilogo'),
        ),
    ]
