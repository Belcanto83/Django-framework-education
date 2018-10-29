# Generated by Django 2.1.2 on 2018-10-27 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', upload_to='products'),
            preserve_default=False,
        ),
    ]
