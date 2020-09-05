from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.http import is_safe_url
from django.views.decorators.csrf import csrf_protect, csrf_exempt

STRIPE_PUB_KEY = 'pk_test_51HNHrgBlsosESXXHVC5Yy5mNFd04M0DK9PMfZROJPgLTkF1oF2Na9vDfXsDoEOAXXD9xUQuDeZAs3HfoE2ZQkCDI007J2P3vXi'


def payment_method_view(request):
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, 'billing/payment-method.html', context={
        'publish_key': STRIPE_PUB_KEY,
        'next_url': next_url
    })


def payment_method_create_view(request):
    if request.method == 'POST' and request.is_ajax():
        print(request.POST)
        return JsonResponse({'message': 'Done'})
    return HttpResponse('error', status=401)
