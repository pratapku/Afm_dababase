# Generated by Django 4.0.6 on 2022-07-21 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alldevices_device_field_place_subuseraccess_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alldevices',
            old_name='allDevices_id_id',
            new_name='allDevices_id',
        ),
    ]
