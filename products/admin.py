from django.contrib import admin

from . import models

from django_summernote.admin import SummernoteModelAdmin


class VariationInLine(admin.TabularInline):
    model = models.Variation
    extra = 1


class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'product_name',
        'short_description',
        'get_price_marketing_br',
        'get_price_marketing_promotional_br',
    )
    summernote_fields = ('description',)
    inlines = [
        VariationInLine
    ]


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Variation)
