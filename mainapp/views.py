from django.shortcuts import render

from mainapp.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'GeekShop',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)

