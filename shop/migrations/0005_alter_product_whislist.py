# Generated by Django 4.1.10 on 2023-09-24 08:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0004_product_whislist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='whislist',
            field=models.ManyToManyField(blank=True, related_name='whislist', to=settings.AUTH_USER_MODEL),
        ),
    ]