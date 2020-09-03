from django.shortcuts import render

STRIPE_PUB_KEY = 'pk_test_51HNHrgBlsosESXXHVC5Yy5mNFd04M0DK9PMfZROJPgLTkF1oF2Na9vDfXsDoEOAXXD9xUQuDeZAs3HfoE2ZQkCDI007J2P3vXi'

def payment_method_view(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'billing/payment-method.html', context={})
