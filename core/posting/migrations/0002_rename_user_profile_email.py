# Generated by Django 5.0.2 on 2024-03-01 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posting", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="user",
            new_name="email",
        ),
    ]