# Generated by Django 5.0.2 on 2024-04-03 00:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posting", "0007_alter_relation_follower"),
    ]

    operations = [
        migrations.AlterField(
            model_name="relation",
            name="followed",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="followers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="relation",
            name="follower",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="following",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
