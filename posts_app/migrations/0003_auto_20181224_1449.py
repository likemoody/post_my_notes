# Generated by Django 2.1.1 on 2018-12-24 14:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0002_auto_20181223_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_read',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
