# Generated by Django 4.0.1 on 2022-01-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_alter_collection_main_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='main_image',
            field=models.ImageField(upload_to='collection'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='secondary_image',
            field=models.ImageField(upload_to='collection'),
        ),
    ]
