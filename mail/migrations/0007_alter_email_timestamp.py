# Generated by Django 4.1.2 on 2022-11-01 04:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0006_alter_email_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 4, 51, 56, 213737, tzinfo=datetime.timezone.utc)),
        ),
    ]
