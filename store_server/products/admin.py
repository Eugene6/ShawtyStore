from django.contrib import admin

from products.models import ProductCategory, Product, Basket

# admin.site.register(ProductCategory)
admin.site.register(Basket)

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    readonly_fields = ('price', 'category')
    search_fields = ('name',)

class BasketAdminInLine(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp', 'product')
    extra = 0

@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    ordering = ('name',)
