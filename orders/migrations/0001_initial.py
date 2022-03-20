# Generated by Django 4.0.3 on 2022-03-19 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='total')),
                ('status', models.CharField(choices=[('A', 'Aprovado'), ('C', 'Criado'), ('R', 'Reprovado'), ('P', 'Pendente'), ('E', 'Enviado'), ('F', 'Finalizado')], max_length=50, verbose_name='status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuário')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='ItenOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255, verbose_name='produto')),
                ('product_id', models.PositiveIntegerField(verbose_name='produto ID')),
                ('variation', models.CharField(max_length=255, verbose_name='variação')),
                ('variation_id', models.PositiveIntegerField(verbose_name='variação ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='preço')),
                ('price_promotional', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='preço promocional')),
                ('quantity', models.PositiveIntegerField(verbose_name='quantidade')),
                ('image', models.CharField(max_length=2000, verbose_name='imagem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='pedido')),
            ],
            options={
                'verbose_name': 'Item Pedido',
                'verbose_name_plural': 'Itens Pedido',
            },
        ),
    ]
