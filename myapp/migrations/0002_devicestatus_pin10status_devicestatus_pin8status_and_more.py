# Generated by Django 4.0.6 on 2022-07-31 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicestatus',
            name='pin10Status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='devicestatus',
            name='pin8Status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='devicestatus',
            name='pin9Status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='devicestatus',
            name='sensor10',
            field=models.FloatField(blank=True, default=0.0, max_length=50),
        ),
        migrations.AddField(
            model_name='devicestatus',
            name='sensor8',
            field=models.FloatField(blank=True, default=0.0, max_length=50),
        ),
        migrations.AddField(
            model_name='devicestatus',
            name='sensor9',
            field=models.FloatField(blank=True, default=0.0, max_length=50),
        ),
    ]