# Generated by Django 2.2.8 on 2020-04-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20200411_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='es_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
