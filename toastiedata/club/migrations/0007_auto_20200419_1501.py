# Generated by Django 2.2.12 on 2020-04-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_auto_20200419_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathwaylevel',
            name='title',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='pathwayspeech',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
