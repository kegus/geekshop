from django.shortcuts import render

from mainapp.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'mainapp/index.html')


# def products(request, category_id=None):
#     context = {'categories': ProductCategory.objects.all(),
#                'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all(),
#     }
#     return render(request, 'mainapp/products.html', context)

def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('price')
    else:
        products = Product.objects.all().order_by('-price')
    paginator = Paginator(object_list=products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(page=1)
    except EmptyPage:
        products_paginator = paginator.page(page=paginator.num_pages)
    context = {'categories': ProductCategory.objects.all(), 'products': products_paginator}
    return render(request, 'mainapp/products.html', context)
