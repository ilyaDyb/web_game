# Generated by Django 4.2.7 on 2024-03-23 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_boosts_user_auto_click_user_tap_ability'),
        ('boosts', '0003_remove_boosts_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Boosts',
        ),
    ]