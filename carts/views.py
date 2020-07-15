from django.shortcuts import render
from .models import Cart


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    items =  cart_obj.items.all()
    total = 0
    for i in items:
        total += i.price
    # create cart
    cart_obj.total = total
    cart_obj.save()
    return render(request, 'carts/home.html')