# Generated by Django 2.0.5 on 2018-05-24 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atApt', '0002_joiner'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_customer',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
