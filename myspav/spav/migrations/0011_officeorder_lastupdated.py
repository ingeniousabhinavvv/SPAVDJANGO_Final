# Generated by Django 4.0.4 on 2022-05-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0010_officeorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='officeorder',
            name='lastUpdated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
