# Generated by Django 4.0.5 on 2022-08-26 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_userinfo_price_history_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='light_mode',
            field=models.BooleanField(default=False),
        ),
    ]