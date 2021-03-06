# Generated by Django 3.0.7 on 2020-07-04 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("club", "0011_meeting_club"),
    ]

    operations = [
        migrations.CreateModel(
            name="Award",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="MemberAward",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "award",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="club.Role"
                    ),
                ),
                (
                    "meeting",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="club.Meeting"
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="club.Member"
                    ),
                ),
            ],
        ),
    ]
