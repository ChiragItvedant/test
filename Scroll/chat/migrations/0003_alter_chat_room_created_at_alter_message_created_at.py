# Generated by Django 5.0.2 on 2024-03-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_message_by_user_remove_message_to_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_room',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]