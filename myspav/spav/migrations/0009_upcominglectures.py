# Generated by Django 4.0.4 on 2022-05-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0008_faculty_facultyimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upcominglectures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lectureTitle', models.CharField(max_length=250)),
                ('lectureDate', models.DateField(auto_now_add=True)),
                ('lectreLink', models.URLField(max_length=500, null=True)),
                ('lectreBanner', models.FileField(upload_to='lecture')),
            ],
        ),
    ]
