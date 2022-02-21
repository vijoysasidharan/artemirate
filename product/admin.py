from django.contrib import admin
from . models import Product, ProductGallery, Variant
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name', )}
    list_display = ('product_name', 'old_price', 'new_price', 'stock', 'collection', 'is_available')
    inlines = [ProductGalleryInline]
    list_per_page = 15
    list_filter = ('collection',)
    search_fields = ['product_name']

class VariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'category', 'value', 'is_active')
    list_editable = ('is_active', )
    list_filter = ('product', 'category', 'value')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
admin.site.register(Variant, VariantAdmin)
