# Generated by Django 4.0.6 on 2022-07-28 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_tempuser_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='p_id',
            new_name='place_id',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='p_type',
            new_name='place_type',
        ),
    ]