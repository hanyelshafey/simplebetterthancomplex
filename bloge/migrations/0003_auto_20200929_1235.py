# Generated by Django 3.1.1 on 2020-09-29 12:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bloge', '0002_post_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='active',
            new_name='poststatus',
        ),
        migrations.AlterField(
            model_name='post',
            name='savetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
