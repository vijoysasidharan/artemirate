from django.db import models

# Create your models here.
class ProductMaterial(models.Model):
    material_name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name                = 'Product Material'
        verbose_name_plural         = 'Product Materials'

    def __str__(self):
        return self.material_name

class ProductType(models.Model):
    type_name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name                = 'Product Type'
        verbose_name_plural         = 'Product Types'

    def __str__(self):
        return self.type_name
    
class ProductShape(models.Model):
    shape_name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name                = 'Product Shape'
        verbose_name_plural         = 'Product Shapes'

    def __str__(self):
        return self.shape_name
    
class ProductUsage(models.Model):
    usage_name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name                = 'Product Usage'
        verbose_name_plural         = 'Product Usages'

    def __str__(self):
        return self.usage_name
