# Generated by Django 4.1.10 on 2023-09-24 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_remove_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.FileField(blank=True, upload_to='products/'),
        ),
    ]
