from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Order(models.Model):
    """Model definition for Pedido."""

    # TODO: Define fields here
    user = models.ForeignKey(
        get_user_model(),
        verbose_name=_('usuário'),
        on_delete=models.CASCADE,
    )
    total = models.DecimalField(
        verbose_name=_('total'),
        max_digits=5,
        decimal_places=2
    )
    status = models.CharField(
        verbose_name=_('status'),
        max_length=50,
        choices=(
            ('A', _('Aprovado')),
            ('C', _('Criado')),
            ('R', _('Reprovado')),
            ('P', _('Pendente')),
            ('E', _('Enviado')),
            ('F', _('Finalizado')),
        )
    )

    class Meta:
        """Meta definition for Pedido."""

        verbose_name = _('Pedido')
        verbose_name_plural = _('Pedidos')

    def __str__(self):
        """Unicode representation of Pedido."""
        return _(f'Pedido número {self.pk}')


class ItenOrder(models.Model):
    """Model definition for ItenOrder."""

    # TODO: Define fields here
    order = models.ForeignKey(
        Order,
        verbose_name=_('pedido'),
        on_delete=models.CASCADE,
    )
    product = models.CharField(
        verbose_name=_('produto'),
        max_length=255,
    )
    product_id = models.PositiveIntegerField(
        verbose_name=_('produto ID'),
    )
    variation = models.CharField(
        verbose_name=_('variação'),
        max_length=255,
    )
    variation_id = models.PositiveIntegerField(
        verbose_name=_('variação ID'),
    )
    price = models.DecimalField(
        verbose_name=_('preço'),
        max_digits=5,
        decimal_places=2,
    )
    price_promotional = models.DecimalField(
        verbose_name=_('preço promocional'),
        max_digits=5,
        decimal_places=2,
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_('quantidade'),
    )
    image = models.CharField(
        verbose_name=_("imagem"),
        max_length=2000,
    )

    class Meta:
        """Meta definition for ItenOrder."""

        verbose_name = 'Item Pedido'
        verbose_name_plural = 'Itens Pedido'

    def __str__(self):
        """Unicode representation of ItenOrder."""
        return _(f'Item do Pedido Nº {self.order.pk}')
