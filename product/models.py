from email.mime import image
from email.policy import default
from itertools import product
from statistics import mode
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from collection.models import Collection

# Create your models here.

class Product(models.Model):
    product_name                    = models.CharField(max_length=200, unique=True)
    slug                            = models.SlugField(max_length=200, unique=True)
    description                     = models.TextField(max_length=500, blank=True)
    old_price                       = models.IntegerField()
    new_price                       = models.IntegerField()
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

