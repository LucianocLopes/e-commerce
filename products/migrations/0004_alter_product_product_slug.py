# Generated by Django 4.0.3 on 2022-03-19 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.SlugField(blank=True, max_length=2000, null=True, verbose_name='slug'),
        ),
    ]
