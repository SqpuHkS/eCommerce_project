from django.shortcuts import render, redirect
from .models import Cart
from items.models import Item



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

def cart_update(request):
    item_id = 3
    item_obj = Item.objects.get(id = item_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_obj.items.add(item_obj)
    return redirect('cart:home')