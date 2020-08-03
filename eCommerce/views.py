from django.shortcuts import render, redirect

def main_page(request):
    if request.user.is_authenticated:
        return render(request, 'home_page.html', context={'username': request.user.username})
    return render(request, 'home_page.html')

