# Generated by Django 3.2.6 on 2021-08-20 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0004_auto_20210820_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gnd_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
