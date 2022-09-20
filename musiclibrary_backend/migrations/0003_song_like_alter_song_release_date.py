# Generated by Django 4.1.1 on 2022-09-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiclibrary_backend', '0002_song_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='like',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]