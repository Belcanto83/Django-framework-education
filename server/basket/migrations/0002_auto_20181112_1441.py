# Generated by Django 2.1.2 on 2018-11-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial_'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedproducts',
            name='ordered_products_qty',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
