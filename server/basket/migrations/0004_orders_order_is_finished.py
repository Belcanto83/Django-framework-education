# Generated by Django 2.1.2 on 2018-11-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_auto_20181112_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
