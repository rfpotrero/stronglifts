from django.shortcuts import render
from .models import Product


def memberships(request):
    """ View To display all memberships """

    all_memberships = Product.objects.filter(category="1")

    context = {
        'all_memberships': all_memberships
    }
    return render(request, 'products/memberships.html', context)