from django.db import models
from collection.models import Collection
from web.models import *
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name                    = models.CharField(max_length=200, unique=True)
    slug                            = models.SlugField(max_length=200, unique=True)
    description                     = models.TextField(max_length=500, blank=True)
    material                        = models.ForeignKey(ProductMaterial, on_delete=models.CASCADE, null=True)
    type                            = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True)
    shape                           = models.ForeignKey(ProductShape, on_delete=models.CASCADE, null=True)
    usage                           = models.ForeignKey(ProductUsage, on_delete=models.CASCADE, null=True)
    old_price                       = models.DecimalField(max_digits=7, decimal_places=2)
    new_price                       = models.DecimalField(max_digits=7, decimal_places=2)
    main_image                      = models.ImageField(upload_to="products")
    second_image                    = models.ImageField(upload_to="products", blank=True)
    stock                           = models.IntegerField()
    is_available                    = models.BooleanField(default=True)
    featured_product                = models.BooleanField(default=False)
    collection                      = models.ForeignKey(Collection, on_delete=models.CASCADE)
    created_on                      = models.DateTimeField(auto_now_add=True)
    updated_on                      = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name                = 'Product'
        verbose_name_plural         = 'Products'
    
    def get_slug_url(self):
        return reverse('product_detail', args=[self.collection.slug, self.slug])

    def __str__(self):
        return self.product_name

class ProductGallery(models.Model):
    product                         = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image                           = models.ImageField(upload_to="products")

    class Meta:
        verbose_name                = 'Product Gallery'
        verbose_name_plural         = 'Product Gallery'

    def __str__(self):
        return self.product.product_name

class VariantManager(models.Manager):
    def colors(self):
        return super(VariantManager, self).filter(category='color', is_active=True)
    def sizes(self):
        return super(VariantManager, self).filter(category='size', is_active=True)
    def finishings(self):
        return super(VariantManager, self).filter(category='finishing', is_active=True)

variant_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
    ('finishing', 'finishing'),
)

class Variant(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    category    = models.CharField(max_length=100, choices=variant_category_choice)
    value       = models.CharField(max_length=100)
    is_active   = models.BooleanField(default=True)
    created_on  = models.DateTimeField(auto_now=True)

    objects = VariantManager()

    class Meta:
        verbose_name                = 'Product Variant'
        verbose_name_plural         = 'Product Variants'

    def __str__(self):
        return self.value
    


