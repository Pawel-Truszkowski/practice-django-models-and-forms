from django.contrib import admin
from django.db.models import F

from .models import Product


@admin.action(description= "Apply discount")
def discount_10_percent(modeladmin, request, queryset):
    queryset.update(price= F('price') * 0.9)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_stock']

    actions = [discount_10_percent]


admin.site.register(Product, ProductAdmin)