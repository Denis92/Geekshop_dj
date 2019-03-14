from django.contrib import admin
from .models import ProductCategory, Product


class ProductInline(admin.TabularInline):
    model = Product
    fields = 'name', 'short_desc'
    extra = 2


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    inlines = ProductInline,


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = 'hot_offer',
    search_fields = 'name',
