# Generated by Django 4.0.1 on 2022-01-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'verbose_name': 'Collection', 'verbose_name_plural': 'Collections'},
        ),
        migrations.AlterField(
            model_name='collection',
            name='featured_collection',
            field=models.BooleanField(default=False),
        ),
    ]
