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
    if collection_slug != None:
        collection = get_object_or_404(Collection, slug=collection_slug)
        products = Product.objects.all().filter(collection = collection, is_available = True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available = True)
        products_count = products.count()
    
    context = {
        'collection': collection,
        'products': products,
        'products_count': products_count
    }
    return render(request, 'products.html', context)

def product_detail(request, collection_slug, product_slug):
    try:
        single_product = Product.objects.get(collection__slug=collection_slug, slug=product_slug)
    except Exception as ex:
        raise ex

    context = {
        'single_product': single_product,
    }    
    return render(request, 'product_detail.html', context)

def cart(request):
    return render(request, 'cart.html')