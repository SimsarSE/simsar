# Generated by Django 2.0.9 on 2018-12-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_auto_20181217_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='is_end',
            field=models.BooleanField(default=False),
        ),
    ]
