# Generated by Django 4.1 on 2023-11-27 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0004_alter_grain_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='grain',
            name='img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media'),
        ),
    ]