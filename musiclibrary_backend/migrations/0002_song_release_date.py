# Generated by Django 4.1.1 on 2022-09-16 18:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musiclibrary_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
