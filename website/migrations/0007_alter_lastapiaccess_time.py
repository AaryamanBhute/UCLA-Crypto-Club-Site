# Generated by Django 4.0.5 on 2022-08-20 23:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_lastapiaccess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastapiaccess',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
