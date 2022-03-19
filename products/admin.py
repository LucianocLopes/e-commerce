from django.contrib import admin
from . import models


class VariationInLine(admin.TabularInline):
    model = models.Variation
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        VariationInLine
    ]


admin.site.register(models.Variation)
