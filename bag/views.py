"Bag app views.py"
from django.shortcuts import render


def view_bag(request):
    "A view for the bag page"
    return render(request, 'bag/bag.html')
