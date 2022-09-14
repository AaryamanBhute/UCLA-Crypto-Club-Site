# Generated by Django 4.0.5 on 2022-09-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_guestuserinfo_is_guest_userinfo_is_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestuserinfo',
            name='leaderboard_portfolio_value',
            field=models.DecimalField(decimal_places=50, default=40000, max_digits=500),
        ),
        migrations.AddField(
            model_name='guestuserinfo',
            name='price_history',
            field=models.TextField(default='40000'),
        ),
    ]