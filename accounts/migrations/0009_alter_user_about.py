# Generated by Django 3.2.3 on 2021-11-20 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20211120_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, max_length=250, verbose_name='about'),
        ),
    ]