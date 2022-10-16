# Generated by Django 4.1.2 on 2022-10-16 00:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 16, 0, 21, 38, 875960, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 16, 0, 21, 38, 876961, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 16, 0, 21, 38, 861959, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profits',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 16, 0, 21, 38, 876961, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 16, 0, 21, 38, 876961, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='profile/avatar.png', upload_to='profile/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]