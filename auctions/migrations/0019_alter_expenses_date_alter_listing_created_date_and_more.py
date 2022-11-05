# Generated by Django 4.1.2 on 2022-11-05 16:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_alter_comment_created_date_alter_expenses_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='profits',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]