# Generated by Django 3.2.9 on 2021-11-04 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20211104_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishgame',
            name='release_date',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]