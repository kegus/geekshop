from django.contrib import admin

from mainapp.models import ProductCategory, Product

# admin.site.register(ProductCategory)

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    readonly_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity',)
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category',)
    readonly_fields = ('short_description',)
    ordering = ('price', '-name',)
    search_fields = ('name', 'category__name',)
