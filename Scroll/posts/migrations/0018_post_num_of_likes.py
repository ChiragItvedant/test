# Generated by Django 5.0.2 on 2024-03-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_post_created_at_post_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='num_of_likes',
            field=models.BigIntegerField(default=0),
        ),
    ]