from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart: 
        messages.error(request, "Your cart in Empty")
        return redirect(reverse('home'))
    
    order_form = OrderForm()

    context = {
        'order_form': order_form,
    }