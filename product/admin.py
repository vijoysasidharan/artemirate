from django.contrib import admin
from . models import Product, ProductGallery
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


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
