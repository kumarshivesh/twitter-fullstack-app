# Generated by Django 5.0.7 on 2024-08-11 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0008_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='coverimg',
            field=models.ImageField(default='blank-cover-picture.png', upload_to='cover_images'),
        ),
    ]
