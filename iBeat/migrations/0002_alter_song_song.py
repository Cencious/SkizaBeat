# Generated by Django 4.0.6 on 2022-07-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iBeat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.FileField(upload_to='songs/'),
        ),
    ]
