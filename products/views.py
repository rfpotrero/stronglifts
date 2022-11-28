from django.shortcuts import render


def memberships(request):
    return render(request, 'products/memberships.html')