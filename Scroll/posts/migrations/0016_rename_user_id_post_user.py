# Generated by Django 5.0.2 on 2024-02-28 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_post_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='user',
        ),
    ]