from django.shortcuts import render
from .models import Product


def memberships(request):
    """ View To display all memberships """

    all_memberships = Product.objects.filter(category="1")

    context = {
        'all_memberships': all_memberships
    }
    return render(request, 'products/memberships.html', context)


def store(request):
    """ View to display all products"""
    all_products = Product.objects.exclude(category="1")

    context = {
        'all_products': all_products
    }
    return render(request, 'products/store.html', context)

    