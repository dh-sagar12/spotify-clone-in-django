# Generated by Django 3.2.3 on 2021-11-27 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_verificationtoken_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationtoken',
            name='is_valid',
            field=models.BooleanField(default=True),
        ),
    ]
