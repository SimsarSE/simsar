# Generated by Django 2.0.9 on 2018-11-10 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='phone',
            new_name='GSM',
        ),
    ]