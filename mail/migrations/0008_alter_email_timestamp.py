# Generated by Django 4.1.2 on 2022-11-05 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0007_alter_email_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 5, 16, 13, 59, 386903, tzinfo=datetime.timezone.utc)),
        ),
    ]
