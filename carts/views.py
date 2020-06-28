from django.shortcuts import render
from .models import Cart

def cart_create(user=None):
    cart_obj = Cart.objects.new_cart(user)
    return cart_obj

def cart_home(request):
    cart_id = request.session.get('cart_id', None)
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        cart_obj = qs.first()
        if request.user.is_authenticated and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
        # cart_id exists
    else:
        cart_obj = Cart.objects.new_cart(user=request.user)
        request.session['cart_id'] = cart_obj.id
        # create cart
    return render(request, 'carts/home.html')