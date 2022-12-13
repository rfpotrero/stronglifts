from django.shortcuts import render, redirect


def view_cart(request):
    """ View to display the cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ Add to cart products view """
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    return redirect(redirect_url)
