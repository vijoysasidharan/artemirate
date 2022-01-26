from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, CartItem
from product.models import Product, Variant
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create
    return cart

def add_to_cart(request, product_id):
    quantity = 1
    product_variants = []
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        quantity = int(request.POST['quantity'])        
        for item in request.POST:
            key = item
            value = request.POST[key]
            try:
                variant = Variant.objects.get(product=product, category__iexact=key, value__iexact=value)
                product_variants.append(variant)
            except:
                pass
        product_variants = sorted(product_variants, key = str)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request),
        )
    cart.save()
    
    is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
    if is_cart_item_exists:
        cart_item = CartItem.objects.filter(product=product, cart=cart)
        existing_variants_list = []
        cart_item_id = []
        for item in cart_item:
            existing_variants = item.variants.all().order_by('value')
            existing_variants_list.append(list(existing_variants))
            cart_item_id.append(item.id)

        if product_variants in existing_variants_list:
            index = existing_variants_list.index(product_variants)
            item_id = cart_item_id[index]
            item = CartItem.objects.get(product=product, id=item_id)
            item.quantity += quantity
            item.save()
        else:
            item = CartItem.objects.create(product=product, quantity=quantity, cart=cart)
            if len(product_variants) > 0:
                item.variants.clear()
                item.variants.add(*product_variants)
            item.save()
    else:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = quantity,
            cart = cart,
        )
        if len(product_variants) > 0:
            cart_item.variants.clear()
            cart_item.variants.add(*product_variants)
        cart_item.save()
    return redirect('cart')

def remove_from_cart(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')

def remove_cart_item(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.new_price * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)
