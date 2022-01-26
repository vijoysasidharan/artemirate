from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from collection.models import Collection
from product.models import Product
from cart.models import Cart, CartItem
from django.db.models import Q
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def index(request):
    collections = Collection.objects.all().filter(featured_collection = True)
    context = {
        'collections': collections
    }
    return render(request, "index.html", context)

def products(request, collection_slug=None):
    collection = None
    products =None
    if collection_slug != None:
        collection = get_object_or_404(Collection, slug=collection_slug)
        products = Product.objects.all().filter(collection = collection, is_available = True).order_by('id')
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available = True).order_by('id')        
        products_count = products.count()
    
    paginator = Paginator(products, 12) #Numer of products per page
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    
    context = {
        'collection': collection,
        'products': paged_products,
        'products_count': products_count,
    }
    return render(request, 'products.html', context)

def product_detail(request, collection_slug, product_slug):
    try:
        single_product = Product.objects.get(collection__slug=collection_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as ex:
        raise ex

    context = {
        'single_product': single_product,
        'item_in_cart': in_cart,
    }    
    return render(request, 'product_detail.html', context)

def cart(request):
    return render(request, 'cart.html')

def search(request):
    if 'q' in request.GET:
        keyword = request.GET['q']
        if keyword:
            products = Product.objects.order_by('-created_on').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
    context = {
        'products': products,
        'products_count': products.count(),
    }
    return render(request, 'products.html', context)