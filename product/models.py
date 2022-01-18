from statistics import mode
from django.db import models
from collection.models import Collection

# Create your models here.

class Product(models.Model):
    product_name                = models.CharField(max_length=200, unique=True)
    slug                        = models.SlugField(max_length=200, unique=True)
    description                 = models.TextField(max_length=500, blank=True)
    old_price                   = models.IntegerField()
    new_price                   = models.IntegerField()
    main_image                  = models.ImageField(upload_to="products")
    stock                       = models.IntegerField()
    is_available                = models.BooleanField(default=True)
    featured_product            = models.BooleanField(default=False)
    collection                  = models.ForeignKey(Collection, on_delete=models.CASCADE)
    created_on                  = models.DateTimeField(auto_now_add=True)
    updated_on                  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name            = 'Product'
        verbose_name_plural     = 'Products'

    def __str__(self):
        return self.product_name