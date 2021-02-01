from django.shortcuts import render

from mainapp.models import ProductCategory, Product


def index(request):
    return render(request, 'mainapp/index.html')


def products(request, id=None):
    if id:
        context = {
            'product': Product.objects.get(id=id),
        }
    else:
        context = {
            'products': Product.objects.all(),
            'categories': ProductCategory.objects.all(),
        }
    return render(request, 'mainapp/products.html', context)
