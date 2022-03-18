from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserCustomManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('O e-mail é obrigatório'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser precisa ter is_superuser=True'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser precisa ter is_staff=True'))

        return self._create_user(email, password, **extra_fields)


class UserCustom(AbstractUser):
    email = models.EmailField(_('E-mail'), unique=True)
    phone = models.CharField(_('Telefone'), max_length=15)
    is_staff = models.BooleanField(_('Membro da equipe'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self) -> str:
        return self.first_name.strip().title()

    objects = UserCustomManager()
