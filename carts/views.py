from django.shortcuts import render, redirect
from .models import Cart
from items.models import Item



def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'carts/home.html', context={'cart': cart_obj})

def cart_update(request):
    item_id = request.POST.get('item_id')
    if item_id is not None:
        try:
            item_obj = Item.objects.get(id = item_id)
        except Item.DoesNotExist:
            print('Error')
            return redirect('cart:home')
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if item_obj in cart_obj.items.all():
            cart_obj.items.remove(item_obj)
        else:
            cart_obj.items.add(item_obj)
    return redirect('cart:home')