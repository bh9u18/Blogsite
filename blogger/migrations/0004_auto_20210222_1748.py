# Generated by Django 3.1.6 on 2021-02-22 12:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0003_auto_20210216_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 22, 12, 18, 37, 34175, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=250, unique=True),
        ),
    ]