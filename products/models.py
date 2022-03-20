import os
from PIL import Image
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils.text import slugify


class Product(models.Model):
    """Model definition for Produto."""

    # TODO: Define fields here
    product_name = models.CharField(
        verbose_name=_('nome do produto'),
        max_length=255,
    )
    short_description = models.TextField(
        verbose_name=_('descrição curta'),
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_('descrição longa'),
    )
    image = models.ImageField(
        verbose_name=_('imagem'),
        upload_to='product_image/%Y/%m/',
        blank=True,
        null=True,
    )
    product_slug = models.SlugField(
        verbose_name=_('slug'),
        blank=True,
        null=True,
        max_length=2000,
    )
    price_marketing = models.DecimalField(
        verbose_name=_('preço marketing'),
        max_digits=9,
        decimal_places=2,
    )
    price_marketing_promotional = models.DecimalField(
        verbose_name=_('preço marketing promocional'),
        max_digits=9,
        decimal_places=2,
        default=0
    )
    product_type = models.CharField(
        verbose_name=_('tipo de produto'),
        max_length=1,
        choices=(
            ('V', _('Variável')),
            ('S', _('Simples')),
        )
    )

    class Meta:
        """Meta definition for Produto."""

        verbose_name = _('Produto')
        verbose_name_plural = _('Produtos')

    def __str__(self):
        """Unicode representation of Produto."""
        return self.product_name.strip().title()

    def get_price_marketing_br(self):
        return f'R$ {self.price_marketing:.2f}'.replace('.', ',')
    get_price_marketing_br.short_description = _('Preço')

    def get_price_marketing_promotional_br(self):
        return f'R$ {self.price_marketing_promotional:.2f}'.replace('.', ',')
    get_price_marketing_promotional_br.short_description = _('Preço PROMO')

    @staticmethod
    def resize_image(img, new_width=800):
        # recupera o caminha da imagem
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)  # abre a imagem com lib PIL
        # recupera a largura e altura original da imagem
        origin_width, origin_height = img_pil

        # se a imagem fo menor ou igual a largura maxima, retorna sem mexer
        if origin_width <= new_width:
            img_pil.close
            return

        # faz regra de 3 para pegar a nova altura
        new_height = round((new_width * origin_height) / origin_width)
        # define a nova altura e largura
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)

        # sobescreve a imagem redimensionada
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50,
        )

    def save(self, *args, **kwargs):
        if not self.product_slug:
            slug = f'{slugify(self.product_name)}'
            self.product_slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.image:
            self.resize_image(self.image, max_image_size)


class Variation(models.Model):
    """Model definition for Variation."""

    # TODO: Define fields here
    product = models.ForeignKey(
        Product,
        verbose_name=_('produto'),
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name=_('variação'),
        max_length=50,
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        verbose_name=_('preço'),
        max_digits=9,
        decimal_places=2,
    )
    price_promotional = models.DecimalField(
        verbose_name=_('preço promocional'),
        max_digits=9,
        decimal_places=2,
        default=0,
    )
    quantity_stock = models.PositiveIntegerField(
        verbose_name=_('quantidade estoque'),
        default=1,
    )

    class Meta:
        """Meta definition for Variation."""

        verbose_name = _('variação')
        verbose_name_plural = _('variações')

    def __str__(self):
        """Unicode representation of Variation."""
        return self.name or self.product.name
