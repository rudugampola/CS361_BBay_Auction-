# Generated by Django 4.1.2 on 2022-11-01 02:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_comment_created_date_alter_expenses_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 2, 7, 15, 780934, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 2, 7, 15, 782921, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 2, 7, 15, 762922, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profits',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 2, 7, 15, 781921, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 2, 7, 15, 781921, tzinfo=datetime.timezone.utc)),
        ),
    ]
