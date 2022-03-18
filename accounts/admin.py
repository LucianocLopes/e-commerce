from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _
from .forms import UserCustomChangeForm, UserCustomCreateForm
from .models import UserCustom


@admin.register(UserCustom)
class UserAdmin(UserAdmin):
    add_form = UserCustomCreateForm
    form = UserCustomChangeForm
    model = UserCustom
    list_display = ('first_name', 'last_name', 'email', 'phone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Informações Pessoais'), {
         'fields': ('first_name', 'last_name', 'phone')}),
        (_('Permissões'), {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        (_('Datas Importantes'), {'fields': ('last_login', 'date_joined')}),
    )
