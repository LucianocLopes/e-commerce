# Generated by Django 4.0.3 on 2022-03-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='long_description',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=1, verbose_name='descrição longa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(max_length=255, verbose_name='descrição curta'),
        ),
    ]
