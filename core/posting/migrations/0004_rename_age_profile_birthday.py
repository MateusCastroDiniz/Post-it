# Generated by Django 5.0.2 on 2024-03-02 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posting", "0003_alter_post_author"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="age",
            new_name="birthday",
        ),
    ]
