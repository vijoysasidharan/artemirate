# Generated by Django 4.0.1 on 2022-01-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_variant'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variants',
            field=models.ManyToManyField(blank=True, to='product.Variant'),
        ),
    ]
