from django.shortcuts import render, redirect

from billing.models import BillingProfile
from accounts.models import GuestEmail
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
    user = request.user
    billing_profile = None
    login_form = LoginForm()
    guest_form = GuestForm()
    guest_email_id = request.session.get('guest_email_id')

    if user.is_authenticated:
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=user, email=user.email)
    elif guest_email_id is not None:
        guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
        billing_profile, billing_guest_profile_created = BillingProfile.objects.get_or_create(email=guest_email_obj.email)
    else:
        pass
    if billing_profile is not None:
        order_qs = Order.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)

        if order_qs.count() == 1:
            order_obj = order_qs.first()
        else:
            old_order_qs = Order.objects.exclude(billing_profile=billing_profile).filter(cart=cart_obj, active=True)
            if old_order_qs.exists():
                old_order_qs.update(active=False)
            order_obj = Order.objects.create(billing_profile=billing_profile, cart=cart_obj)
    context = {
        'billing_profile': billing_profile,
        'object': order_obj,
        'login_form': login_form,
        'guest_form': guest_form,
    }
    return render(request, 'carts/checkout.html', context)