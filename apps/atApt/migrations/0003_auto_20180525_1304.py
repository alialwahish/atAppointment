# Generated by Django 2.0.5 on 2018-05-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atApt', '0002_auto_20180525_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='appointment_date',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointments',
            name='appointment_time',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
