from django.http import JsonResponse
from django.shortcuts import render, redirect

from addresses.forms import AddressForm
from accounts.forms import GuestForm, LoginForm

from addresses.models import Address
from billing.models import BillingProfile
from .models import Cart
from items.models import Item
from orders.models import Order

from conf import STRIPE_PUB_KEY


def cart_detail_api_view(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    items = [{'title': x.title, 'price': x.price, 'id': x.id} for x in cart_obj.items.all()]
    return JsonResponse({'items': items, 'total': cart_obj.total, 'subtotal': cart_obj.subtotal})

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
            added = False
            id = item_obj.id
        else:
            cart_obj.items.add(item_obj)
            added = True
            id = item_obj.id

        request.session['cart_total'] = cart_obj.items.count()
        if request.is_ajax():
            data = {
                'added': added,
                'cart_total': request.session['cart_total'],
                'id': id,
            }
            return JsonResponse(data)

    return redirect('cart:home')

def checkout_home(request):

    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None

    if cart_created or cart_obj.items.count() == 0:
        return redirect('cart:home')

    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()

    billing_address_id = request.session.get('billing_address_id', None)
    shipping_address_id = request.session.get('shipping_address_id', None)


    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    has_card = False

    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session['shipping_address_id']
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session['billing_address_id']
        if billing_address_id or shipping_address_id:
            order_obj.save()
        has_card = billing_profile.has_card

    #Check that order is done
    if request.method == 'POST':
        if order_obj.check_done():
            did_charge, crg_msg = billing_profile.charge(order_obj)
            if did_charge:
                order_obj.mark_paid()
                del request.session['cart_id']
                request.session['cart_total'] = 0
                if billing_profile.user is None:
                    billing_profile.set_cards_inactive() #do the all cards inactive
                return redirect('cart:success')
            else:
                print(crg_msg)
                return redirect('cart:checkout')
    context = {
        'billing_profile': billing_profile,
        'object': order_obj,
        'login_form': login_form,
        'guest_form': guest_form,
        'address_form': address_form,
        'has_card': has_card,
        'publish_key': STRIPE_PUB_KEY,
    }

    return render(request, 'carts/checkout.html', context)

def checkout_done(request):
    return render(request, 'carts/success.html')