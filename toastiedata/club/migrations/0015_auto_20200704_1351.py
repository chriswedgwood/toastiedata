# Generated by Django 3.0.7 on 2020-07-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("club", "0014_auto_20200704_1343"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member", name="es_id", field=models.IntegerField(unique=True),
        ),
    ]
