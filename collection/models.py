from django.urls import reverse
from django.db import models

# Create your models here.

class Collection(models.Model):
    collection_name         = models.CharField(unique=True, max_length=50)
    slug                    = models.SlugField(unique=True, max_length=100)
    description             = models.TextField(max_length=250, blank=True)
    main_image              = models.ImageField(upload_to="collection")
    secondary_image         = models.ImageField(upload_to="collection")
    featured_collection     = models.BooleanField(default=False)

    class Meta:
        verbose_name        = 'Collection'
        verbose_name_plural = 'Collections'

    def get_slug_url(self):
        return reverse('poducts_by_collection', args=[self.slug])

    def __str__(self):
        return self.collection_name
