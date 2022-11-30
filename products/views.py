from django.shortcuts import render
from .models import Product, Category


def memberships(request):
    """ View To display all memberships """

    all_memberships = Product.objects.filter(category="1")

    context = {
        'all_memberships': all_memberships
    }
    return render(request, 'products/memberships.html', context)


def store(request):
    """ View to display all products and sort by category"""
    products = Product.objects.exclude(category="1")

    if request.GET:
        if 'category' in request.GET:
            products = Product.objects.filter(category=request.GET['category'])
            print(products)

    context = {
        'products': products,
    }
    return render(request, 'products/store.html', context)
