# Generated by Django 3.2.15 on 2022-08-27 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='img_count',
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
