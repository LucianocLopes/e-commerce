import re
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.forms import ValidationError

from utils.validacpf import valida_cpf


class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here
    user = models.OneToOneField(
        get_user_model(),
        verbose_name=_('usuário'),
        on_delete=models.CASCADE,
    )
    birth_date = models.DateField(
        verbose_name=_('data de nascimento'),
    )
    cpf_number = models.CharField(
        verbose_name=_('CPF'),
        max_length=11,
    )
    address = models.CharField(
        verbose_name=_('endereço'),
        max_length=50,
    )
    number = models.CharField(
        verbose_name=_('número'),
        max_length=5,
    )
    complement = models.CharField(
        verbose_name=_('complemento'),
        max_length=30,
    )
    district = models.CharField(
        verbose_name=_('bairro'),
        max_length=30,
    )
    zip_code = models.CharField(
        verbose_name=_('CEP'),
        max_length=8,
    )
    city = models.CharField(
        verbose_name=_('cidade'),
        max_length=50,
    )
    state = models.CharField(
        verbose_name=_('UF'),
        max_length=2,
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfís'

    @property
    def age(self):
        age = self.birth_date - timezone.now

        return int(age)

    @property
    def full_name(self):

        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.user.first_name

    def clean(self):
        error_messages = {}

        if not valida_cpf(self.cpf_number):
            error_messages['cpf_number'] = _('Digite um CPF válido')

        if re.search(r'[^0-9]', self.zip_code) or len(self.zip_code) < 8:
            error_messages['zip_code'] = _(
                'CEP inválido, digite os 8 digitos do CEP.')

        if error_messages:
            raise ValidationError(error_messages)
