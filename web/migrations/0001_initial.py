# Generated by Django 4.0.1 on 2022-02-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Product Material',
                'verbose_name_plural': 'Product Materials',
            },
        ),
        migrations.CreateModel(
            name='ProductShape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Product Shape',
                'verbose_name_plural': 'Product Shapes',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Product Type',
                'verbose_name_plural': 'Product Types',
            },
        ),
        migrations.CreateModel(
            name='ProductUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Product Usage',
                'verbose_name_plural': 'Product Usages',
            },
        ),
    ]
