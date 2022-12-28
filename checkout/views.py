from django.shortcuts import render, redirect, reverse
from django.contrib import messages


from .forms import OrderForm


def checkout(request):
    """Check out view"""
    cart = request.session.get('cart', {})
    if not cart: 
        messages.error(request, "Your cart in Empty")
        return redirect(reverse('view_cart'))
    
    order_form = OrderForm()

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
    }

    return render(request, template, context)