# Generated by Django 4.1 on 2023-11-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0003_grain_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grain',
            name='region',
            field=models.CharField(max_length=100),
        ),
    ]
