# Generated by Django 4.0.6 on 2022-07-31 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_user_subuseraccess_emailtest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subuseraccess',
            name='emailtest',
            field=models.EmailField(max_length=254),
        ),
    ]