# Generated by Django 5.0.2 on 2024-03-03 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posting", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthday",
            field=models.DateTimeField(verbose_name="birthday"),
        ),
    ]
