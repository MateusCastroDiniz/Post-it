# Generated by Django 5.0.2 on 2024-04-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posting", "0010_alter_relation_followed_alter_relation_follower"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="text_content",
            field=models.TextField(blank=True),
        ),
    ]
