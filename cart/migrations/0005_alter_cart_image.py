# Generated by Django 3.2.15 on 2022-09-02 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='image',
            field=models.ImageField(max_length=250, upload_to=''),
        ),
    ]
