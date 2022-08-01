# Generated by Django 4.0.6 on 2022-08-01 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myapp.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0006_alter_subuseraccess_emailtest'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subuserplace',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='f_id',
            field=models.CharField(default=myapp.utils.create_new_ref_number, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='f_name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='p_id',
            field=models.CharField(default=myapp.utils.create_new_ref_number, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='p_type',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='subuserplace',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.subuseraccess', unique=True),
        ),
    ]
