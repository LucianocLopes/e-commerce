from django.contrib import admin
from . import models


class ItenOrderInLine(admin.TabularInline):
    model = models.ItenOrder
    extra = 1


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    '''Admin View for Order'''

    # list_display = ('',)
    # list_filter = ('',)
    inlines = [
        ItenOrderInLine,
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


admin.site.register(models.ItenOrder)
