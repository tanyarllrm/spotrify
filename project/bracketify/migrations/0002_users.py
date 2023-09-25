# Generated by Django 4.2.4 on 2023-09-25 20:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bracketify", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128)),
                ("last_session_datetime", models.DateTimeField(verbose_name="Timestamp of last session")),
            ],
        ),
    ]
