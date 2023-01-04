from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages


def view_cart(request):
    """ View to display the cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ Add to cart products view """

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        messages.error(request, "The item is already in the cart")
        return redirect(reverse('store'))

    cart[product_id] = 1

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, product_id):
    """ Remove products from cart"""

    cart = request.session.get('cart', {})
    if product_id in list(cart.keys()):
        cart.pop(product_id)

    request.session['cart'] = cart
    return redirect(view_cart)
