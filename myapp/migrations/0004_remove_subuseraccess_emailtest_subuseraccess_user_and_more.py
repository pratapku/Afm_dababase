# Generated by Django 4.0.6 on 2022-07-31 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_alter_field_f_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subuseraccess',
            name='emailtest',
        ),
        migrations.AddField(
            model_name='subuseraccess',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='field',
            name='f_name',
            field=models.CharField(max_length=15),
        ),
    ]
