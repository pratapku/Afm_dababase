# Generated by Django 4.0.6 on 2022-08-02 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myapp.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_remove_device_d_id_remove_device_f_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='allDevices',
            fields=[
                ('d_id', models.CharField(default=0, max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='deviceStatus',
            fields=[
                ('d_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.alldevices')),
                ('pin2Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin1Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin3Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin4Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin5Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin6Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin7Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin8Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin9Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin10Status', models.IntegerField(blank=True, default=0, null=True)),
                ('sensor1', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor2', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor3', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor4', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor5', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor6', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor7', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor8', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor9', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor10', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('pin1Name', models.CharField(blank=True, default='Device1,001', max_length=20, null=True)),
                ('pin2Name', models.CharField(blank=True, default='Device2,001', max_length=20, null=True)),
                ('pin3Name', models.CharField(blank=True, default='Device3,001', max_length=20, null=True)),
                ('pin4Name', models.CharField(blank=True, default='Device4,001', max_length=20, null=True)),
                ('pin5Name', models.CharField(blank=True, default='Device5,001', max_length=20, null=True)),
                ('pin6Name', models.CharField(blank=True, default='Device6,001', max_length=20, null=True)),
                ('pin7Name', models.CharField(blank=True, default='Device7,001', max_length=20, null=True)),
                ('pin8Name', models.CharField(blank=True, default='Device8,001', max_length=20, null=True)),
                ('pin9Name', models.CharField(blank=True, default='Device9,001', max_length=20, null=True)),
                ('pin10Name', models.CharField(blank=True, default='Device10,001', max_length=20, null=True)),
                ('pin11Name', models.CharField(blank=True, default='Device11,001', max_length=20, null=True)),
                ('pin12Name', models.CharField(blank=True, default='Device12,001', max_length=20, null=True)),
                ('pin13Name', models.CharField(blank=True, default='Device13,001', max_length=20, null=True)),
                ('pin14Name', models.CharField(blank=True, default='Device14,001', max_length=20, null=True)),
                ('pin15Name', models.CharField(blank=True, default='Device15,001', max_length=20, null=True)),
                ('pin16Name', models.CharField(blank=True, default='Device16,001', max_length=20, null=True)),
                ('pin17Name', models.CharField(blank=True, default='Device17,001', max_length=20, null=True)),
                ('pin18Name', models.CharField(blank=True, default='Device18,001', max_length=20, null=True)),
                ('pin19Name', models.CharField(blank=True, default='Device19,001', max_length=20, null=True)),
                ('pin20Name', models.CharField(blank=True, default='Device20,001', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='field',
            fields=[
                ('f_id', models.CharField(default=myapp.utils.create_new_ref_number, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('f_name', models.CharField(max_length=15, unique=True)),
                ('p_id', models.ForeignKey(default=1, max_length=10, on_delete=django.db.models.deletion.CASCADE, to='myapp.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_installed', models.DateField(default=myapp.utils.dt)),
                ('d_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.alldevices')),
                ('f_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.field')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tempuser',
            name='d_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.alldevices'),
        ),
        migrations.AddField(
            model_name='tempuser',
            name='device_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.device'),
        ),
        migrations.AddField(
            model_name='tempuser',
            name='f_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.field'),
        ),
    ]
