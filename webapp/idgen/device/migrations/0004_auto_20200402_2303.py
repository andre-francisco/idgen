# Generated by Django 3.0.5 on 2020-04-02 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_auto_20200402_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='os',
            field=models.CharField(default=None, help_text='Device operating system', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='os_version',
            field=models.CharField(default=None, help_text='Device operating system version string', max_length=256),
            preserve_default=False,
        ),
    ]