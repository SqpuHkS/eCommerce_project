from django.shortcuts import render, redirect

from addresses.forms import AddressForm
from billing.models import BillingProfile
from .models import Cart
from items.models import Item
from orders.models import Order
from accounts.forms import GuestForm, LoginForm


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
        request.session['cart_total'] = cart_obj.items.count()
    return redirect('cart:home')

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None

    if cart_created or cart_obj.items.count() == 0:
        return redirect('cart:home')

    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)

    context = {
        'billing_profile': billing_profile,
        'object': order_obj,
        'login_form': login_form,
        'guest_form': guest_form,
        'address_form': address_form,
    }



    return render(request, 'carts/checkout.html', context)