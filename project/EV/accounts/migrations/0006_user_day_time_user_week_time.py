# Generated by Django 5.0.4 on 2024-05-26 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_user_day_time_remove_user_week_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='day_time',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='week_time',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
