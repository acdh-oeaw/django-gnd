# Generated by Django 3.2.6 on 2021-08-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0007_auto_20210821_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gnd_birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='gnd_death_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
