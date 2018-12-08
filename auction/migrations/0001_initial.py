# Generated by Django 2.0.9 on 2018-12-08 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0009_auto_20181119_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.Product')),
                ('min_auction_time', models.IntegerField(verbose_name='Auction period of validity')),
                ('start_time', models.DateTimeField(verbose_name='Start Time')),
            ],
            bases=('product.product',),
        ),
    ]
