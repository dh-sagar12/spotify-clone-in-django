# Generated by Django 3.2.3 on 2021-11-19 17:29

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('artist', models.CharField(default='', max_length=100)),
                ('genre', models.CharField(default='music', max_length=100)),
                ('music_file', models.FileField(blank=True, null=True, upload_to='music')),
                ('music_cover_photo', models.FileField(blank=True, null=True, upload_to='images')),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('streamed', models.IntegerField(default=0)),
                ('uploader', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
    ]
