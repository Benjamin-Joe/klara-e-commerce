from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    "A view to display all of the products"
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Woopsie, Not A Valid Input')
                return redirect(reverse, 'products')
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    "A view to display one specific product clicked on by the user"
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
