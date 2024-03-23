# Generated by Django 4.2.7 on 2024-03-23 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boosts', '0003_remove_boosts_user'),
        ('user', '0002_user_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='boosts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_boosts', to='boosts.boosts'),
        ),
    ]