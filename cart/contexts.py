from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """ Context to display items in the cart view """
    cart_items = []
    total = 0
    cart = request.session.get('cart', {})
    cart_total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        total = quantity * product.price
        cart_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
            'total': total,
        })
        cart_total += total

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total
    }

    return context
