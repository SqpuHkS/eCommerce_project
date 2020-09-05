import stripe
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from .models import BillingProfile

STRIPE_PUB_KEY = 'pk_test_51HNHrgBlsosESXXHVC5Yy5mNFd04M0DK9PMfZROJPgLTkF1oF2Na9vDfXsDoEOAXXD9xUQuDeZAs3HfoE2ZQkCDI007J2P3vXi'


def payment_method_view(request):
    # if request.user.is_authenticated:
    #     billing_profile = request.user.billingprofile
    #     my_customer_id = billing_profile.customer_id

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect('/cart')

    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_,  request.get_host()):
        next_url = next_
    return render(request, 'billing/payment-method.html', context={
        'publish_key': STRIPE_PUB_KEY,
        'next_url': next_url
    })


def payment_method_create_view(request):
    if request.method == 'POST' and request.is_ajax():
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

        if not billing_profile:
            return HttpResponse({'message':"Can't find user."}, status=401)

        token = request.POST.get('token')
        if token is not None:


            card_response = stripe.Customer.create_source(
                billing_profile.customer_id,
                source=token,
            )

        return JsonResponse({'message': 'Success! Your card was added.'})
    return HttpResponse('error', status=401)
