# Generated by Django 4.0.6 on 2022-07-14 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iBeat', '0006_alter_song_duration_alter_song_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='artist',
            new_name='Singer_name',
        ),
    ]