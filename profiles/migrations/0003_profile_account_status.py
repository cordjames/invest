# Generated by Django 3.2.7 on 2023-10-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_status',
            field=models.BooleanField(default=False),
        ),
    ]