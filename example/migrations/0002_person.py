# Generated by Django 3.2.6 on 2021-08-20 12:24

from django.db import migrations, models
import gnd.fields


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gnd_gnd_id', gnd.fields.GndField(max_length=250)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
