# Generated by Django 4.0.1 on 2022-01-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_alter_collection_main_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
