# Generated by Django 4.2.16 on 2024-11-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_alter_friend_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
