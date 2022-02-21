from django.contrib import admin
from web.models import *

# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'material_name')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

class ShapeAdmin(admin.ModelAdmin):
    list_display = ('id', 'shape_name')

class UsageAdmin(admin.ModelAdmin):
    list_display = ('id', 'usage_name')


admin.site.register(ProductMaterial, MaterialAdmin)
admin.site.register(ProductType, TypeAdmin)
admin.site.register(ProductShape, ShapeAdmin)
admin.site.register(ProductUsage, UsageAdmin)
