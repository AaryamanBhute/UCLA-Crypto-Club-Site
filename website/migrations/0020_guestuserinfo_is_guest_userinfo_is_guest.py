# Generated by Django 4.0.5 on 2022-09-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_guestuserinfo_alter_userinfo_added_cash_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestuserinfo',
            name='is_guest',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='is_guest',
            field=models.BooleanField(default=False),
        ),
    ]