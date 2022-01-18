from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from collection.models import Collection
from product.models import Product

# Create your views here.

def index(request):
    collections = Collection.objects.all().filter(featured_collection = True)
    context = {
        'collections': collections
    }
    return render(request, "index.html", context)

def products(request, collection_slug=None):
    collection = None
    products = None
    products_count = 0
    if collection_slug != None:
        collection = get_object_or_404(Collection, slug=collection_slug)
        products = Product.objects.all().filter(collection = collection, is_available = True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available = True)
        if(products.count() > 0):
            products_count = products.count()
    
    context = {
        'collection': collection,
        'products': products,
        'products_count': products_count
    }
    return render(request, 'products.html', context)