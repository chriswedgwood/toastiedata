# Generated by Django 2.2.12 on 2020-04-19 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_auto_20200419_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathway',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
