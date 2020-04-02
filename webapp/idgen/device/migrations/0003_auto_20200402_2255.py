# Generated by Django 3.0.5 on 2020-04-02 22:55

import device.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_auto_20200329_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='identifier',
            field=device.models.RandomIdentifierField(default=device.models.GenerateIdentifier(8, '0123456789ABCDEF'), help_text='Device identifier', max_length=8, primary_key=True, serialize=False),
        ),
    ]