# Generated by Django 4.2.7 on 2024-03-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_boost_user_end_game_user_miner'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=11),
        ),
    ]