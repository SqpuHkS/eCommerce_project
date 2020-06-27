from django.shortcuts import render
from .models import Cart

# Create your views here.
def cart_home(request):
    cart_id = request.session.get('cart_id', None)
    if cart_id is None:
        cart_obj = Cart.objects.create(user=None)
        request.session['cart_id'] = cart_obj.id
        print('Created')
    else:
        cart_obj = Cart.objects.get(id=cart_id)
        print('cart id exists')
    return render(request, 'carts/home.html')