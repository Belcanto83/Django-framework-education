# Generated by Django 2.1.2 on 2018-11-12 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20181112_1416'),
        ('basket', '0002_auto_20181112_1441'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orderedproducts',
            unique_together={('order', 'product')},
        ),
    ]