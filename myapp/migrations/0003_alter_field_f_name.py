# Generated by Django 4.0.6 on 2022-07-31 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_devicestatus_pin10status_devicestatus_pin8status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='f_name',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
