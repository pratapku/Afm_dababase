# Generated by Django 4.0.6 on 2022-07-29 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device_status',
            fields=[
                ('allDevices_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.alldevices')),
                ('pin2Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin1Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin3Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin4Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin5Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin6Status', models.IntegerField(blank=True, default=0, null=True)),
                ('pin7Status', models.IntegerField(blank=True, default=0, null=True)),
                ('sensor1', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor2', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor3', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor4', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor5', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor6', models.FloatField(blank=True, default=0.0, max_length=50)),
                ('sensor7', models.FloatField(blank=True, default=0.0, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pin_name',
            fields=[
                ('allDevices_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.alldevices')),
                ('pin1Name', models.CharField(blank=True, max_length=20, null=True)),
                ('pin2Name', models.CharField(blank=True, max_length=20, null=True)),
                ('pin3Name', models.CharField(blank=True, max_length=20, null=True)),
                ('pin4Name', models.CharField(blank=True, max_length=20, null=True)),
                ('pin5Name', models.CharField(blank=True, max_length=20, null=True)),
                ('pin6Name', models.CharField(blank=True, max_length=20, null=True)),
                ('pin7Name', models.CharField(blank=True, max_length=20, null=True)),
                ('pin8Name', models.CharField(blank=True, max_length=20, null=True)),
                ('pin9Name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='deviceipaddress',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='devicestatus',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='emergencynumber',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='emergencynumber',
            name='user',
        ),
        migrations.RemoveField(
            model_name='energy',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='user',
        ),
        migrations.DeleteModel(
            name='oneHourEnergy',
        ),
        migrations.DeleteModel(
            name='oneyeardata',
        ),
        migrations.DeleteModel(
            name='otptemplogin',
        ),
        migrations.RemoveField(
            model_name='pinname',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='pinschedule',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='pinschedule',
            name='user',
        ),
        migrations.RemoveField(
            model_name='room',
            name='flt_id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='user',
        ),
        migrations.RemoveField(
            model_name='sensors',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='somemodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ssidpassword',
            name='d_id',
        ),
        migrations.DeleteModel(
            name='tempUserVerification',
        ),
        migrations.DeleteModel(
            name='threeyears',
        ),
        migrations.RemoveField(
            model_name='userimages',
            name='user',
        ),
        migrations.RenameField(
            model_name='alldevices',
            old_name='d_id',
            new_name='allDevices_id',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='d_id',
            new_name='allDevices_id',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='tempuser',
            old_name='d_id',
            new_name='allDevices_id',
        ),
        migrations.RenameField(
            model_name='tempuser',
            old_name='p_id',
            new_name='place_id',
        ),
        migrations.RemoveField(
            model_name='device',
            name='r_id',
        ),
        migrations.RemoveField(
            model_name='subuserplace',
            name='id',
        ),
        migrations.RemoveField(
            model_name='subuserplace',
            name='p_id',
        ),
        migrations.RemoveField(
            model_name='tempuser',
            name='flt_id',
        ),
        migrations.RemoveField(
            model_name='tempuser',
            name='r_id',
        ),
        migrations.AddField(
            model_name='device',
            name='field_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.field'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subuserplace',
            name='place_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.place', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempuser',
            name='device_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.device'),
        ),
        migrations.AddField(
            model_name='tempuser',
            name='field_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.field'),
        ),
        migrations.AlterField(
            model_name='subuserplace',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.subuseraccess', unique=True),
        ),
        migrations.DeleteModel(
            name='deviceIpAddress',
        ),
        migrations.DeleteModel(
            name='deviceStatus',
        ),
        migrations.DeleteModel(
            name='emergencyNumber',
        ),
        migrations.DeleteModel(
            name='energy',
        ),
        migrations.DeleteModel(
            name='flat',
        ),
        migrations.DeleteModel(
            name='pinName',
        ),
        migrations.DeleteModel(
            name='pinschedule',
        ),
        migrations.DeleteModel(
            name='room',
        ),
        migrations.DeleteModel(
            name='sensors',
        ),
        migrations.DeleteModel(
            name='SomeModel',
        ),
        migrations.DeleteModel(
            name='ssidPassword',
        ),
        migrations.DeleteModel(
            name='userimages',
        ),
    ]